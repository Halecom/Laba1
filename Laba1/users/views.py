from .utils import hashing
import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RegistrationForm, ChangeForm
from .models import User


# получение данных из бд
def index(request):
    if request.session.get("id"):
        user = User.objects.get(id=request.session["id"])
        users = User.objects.all()
        return render(request, "main/index.html", {"users": users, "user": user})

    return HttpResponseRedirect("/users/register/")



def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            if User.objects.filter(username=form.data["username"]).exists():
                form.add_error("username", "Пользователь уже существует!!!!")
                return render(request, "main/register.html", {"form": form})
            password_salt = str(uuid.uuid4())
            password_hash = hashing(form.data["password"], password_salt)

            user = User.objects.create(
                username=form.data["username"],
                password_hash=password_hash,
                password_salt=password_salt,
            )

            request.session["id"] = user.id
            request.session.set_expiry(300)

            return HttpResponseRedirect('/users/')

    return render(request, "main/register.html", {"form": form})


def logout(request):
    if request.session.get("id"):
        del request.session["id"]

    return HttpResponseRedirect('/users/')

def authorization(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.data["username"]).exists():
                user = User.objects.get(username=form.data["username"])
                password_hash = hashing(form.data["password"], user.password_salt)

                if password_hash == user.password_hash:

                    request.session["id"] = user.id
                    request.session.set_expiry(300)

                    return HttpResponseRedirect('/users/')
                else:
                    form.add_error("password", "Пароль не верный!!!!")
                    return render(request, "main/authorization.html", {"form": form})
            else:
                form.add_error("username", "Пользователь не существует!!!!")
                return render(request, "main/authorization.html", {"form": form})
    return render(request, "main/authorization.html", {"form": RegistrationForm()})

def password_change(request):
    if request.session.get("id"):
        form = ChangeForm(request.POST or None)
        if request.method == "POST":

            if form.is_valid():
                user = User.objects.get(id = request.session.get("id"))
                password_hash = hashing(form.data["oldpassword"], user.password_salt)
                if password_hash == user.password_hash:
                    if form.data["newpassword"] == form.data["acceptpassword"]:

                        user.password_salt = str(uuid.uuid4())
                        user.password_hash = hashing(form.data["newpassword"], user.password_salt)
                        user.save()

                        return HttpResponseRedirect('/users/')

                    else:
                        form.add_error("acceptpassword", "Пароли не совпадают!!!!")
                        return render(request, "main/password_change.html", {"form": form})

                else:
                    form.add_error("oldpassword", "Пароль не верный!!!!")
                    return render(request, "main/password_change.html", {"form": form})

        return render(request, "main/password_change.html", {"form": form})

    else:
        return HttpResponseRedirect('/users/authorization')





