from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect

from carta.forms import CartaForm

@csrf_protect
def index(request):

    doc_template = loader.get_template("carta.html")

    if request.method == "POST":
        form = CartaForm(request.POST)

        if form.is_valid():
            f_form = form.save(False)
            f_form.save()
            return redirect(to="gracias/")

    else:
        form = CartaForm()

    ctx = {"form": form}

    doc = doc_template.render(ctx, request)

    return HttpResponse(doc)

def gracias(request):

    ctx = {}

    doc_template = loader.get_template("gracias.html")
    doc = doc_template.render(ctx)

    return HttpResponse(doc)



