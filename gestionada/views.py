from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from gestionada.forms import loginform, EditUserForm
from gestionada.models import Subdelegacion, DaUser


# Create your views here.
def loginvw(request):
    doc_template = loader.get_template("gestionada/login.html")

    if request.method == "POST":
        form = loginform(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)

                return redirect(to="/gestionada/")

    else:
        form = loginform()

    ctx = {"form": form}

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)

@permission_required("Can change user", login_url="/gestionada/login", raise_exception=False)
def list_users(request):
    users = get_user_model().objects.all()

    ctx = {
        "users": users,
       }

    doc_template = loader.get_template("gestionada/mod_user.html")

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)

@permission_required("Can change user", login_url="/gestionada/login", raise_exception=False)
def mod_users(request, username):
    user = User.objects.get(username=username)

    doc_template = loader.get_template("gestionada/edit_user.html")

    if request.method == "POST":
        form = EditUserForm(request.POST)

        if form.is_valid():
            if form.cleaned_data["username"] != "":
                user.username = form.cleaned_data["username"]
            if form.cleaned_data["email"] != "":
                user.email = form.cleaned_data["email"]

            user.save()

            return redirect(to="/gestionada/user")

    else:
        form = EditUserForm()

    subdelegaciones = []
    for subdelegacion in Subdelegacion.objects.values_list("name"):
        subdelegaciones.append(subdelegacion[0])

    ctx = {"form": form,
           "user": user.username,
           "subdelegaciones": subdelegaciones,
           }

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)

@permission_required("Can change user", login_url="/gestionada/login", raise_exception=False)
def subdelega_edit(request, username):
    if request.method == "POST":
        userid = User.objects.get(username=username).id
        user = DaUser.objects.get(user_id=userid)
        user.subdelegacion = Subdelegacion.objects.get(name=request.POST["subdelegacion"])
        user.save()
        return redirect(to="/gestionada/user")

@permission_required("Can change user", login_url="/gestionada/login", raise_exception=False)
def delete_user(request, username):
    if request.method == "POST":
        user = User.objects.get(username=username)
        user.delete()
        return redirect(to="/gestionada/user")


