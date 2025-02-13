from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from gestionada.forms import EditUserForm, loginform
from gestionada.models import DaUser, Subdelegacion


# Create your views here.
def loginvw(request):
    doc_template = loader.get_template("gestionada/login.html")

    if request.method == "POST":
        form = loginform(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)

                return redirect(to="/gestionada/")

    else:
        form = loginform()

    ctx = {"form": form}

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)


@permission_required(
    "Can change user", login_url="/gestionada/login", raise_exception=False
)
def list_users(request):
    users = get_user_model().objects.all()

    ctx = {
        "users": users,
    }

    doc_template = loader.get_template("gestionada/mod_user.html")

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)


@permission_required(
    "Can change user", login_url="/gestionada/login", raise_exception=False
)
def edit_users(request, username):
    user = User.objects.get(username=username)

    doc_template = loader.get_template("gestionada/edit_user.html")

    if request.method == "POST":

        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.save()

        return redirect(to="/gestionada/user/")

    subdelegaciones = []
    for subdelegacion in Subdelegacion.objects.values_list("name"):
        subdelegaciones.append(subdelegacion[0])

    ctx = {
        "user": user.username,
        "subdelegaciones": subdelegaciones,
        "username": user.username,
        "email": user.email,
    }

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)


@permission_required(
    "Can change user", login_url="/gestionada/login", raise_exception=False
)
def subdelega_edit(request, username):
    if request.method == "POST":
        userid = User.objects.get(username=username).id
        user = DaUser.objects.get(user_id=userid)
        user.subdelegacion = Subdelegacion.objects.get(
            name=request.POST["subdelegacion"]
        )
        user.save()
        return redirect(to="/gestionada/user")


@permission_required(
    "Can change user", login_url="/gestionada/login", raise_exception=False
)
def delete_user(request, username):
    if request.method == "POST":
        user = User.objects.get(username=username)
        user.delete()
        return redirect(to="/gestionada/user")


@permission_required(
    "Can change user", login_url="/gestionada/login", raise_exception=False
)
def create_user(request):
    doc_template = loader.get_template("gestionada/create_user.html")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=request.POST["email"],
                password=form.cleaned_data["password1"],
            )
            dauser = DaUser.objects.create(
                user_id=user.id,
                subdelegacion_id=Subdelegacion.objects.get(
                    name=request.POST["subdelegacion"]
                ).id,
            )

            user.save()
            dauser.save()

            return redirect(to="/gestionada/")

    else:
        form = UserCreationForm()

    subdelegaciones = []
    for subdelegacion in Subdelegacion.objects.values_list("name"):
        subdelegaciones.append(subdelegacion[0])

    ctx = {
        "form": form,
        "subdelegaciones": subdelegaciones,
    }

    doc = doc_template.render(ctx, request)
    return HttpResponse(doc)


@login_required(login_url="/gestionada/login/")
def logout_user(request):
    logout(request)
    return redirect(to="/gestionada/")


@login_required(login_url="/gestionada/login/")
def list_cartas(request):
    doc_template = loader.get_template("gestionada/list_cartas.html")

    ctx = {}

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)
