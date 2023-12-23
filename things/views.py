from django.shortcuts import render, redirect
from .models import Things
from .forms import ThingForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# CRUD - create, retrieve, update, delete, list

def thing_list(request):
    things = Things.objects.all()
    context = {
        "things": things
    }
    return render(request, "things.html", context)

def thing_retrieve(request, pk):
    thing = Things.objects.get(id=pk)
    context = {
        "thing": thing
    }
    return render(request, "thing.html", context)

@login_required(login_url='/admin/')
def thing_create(request):
    form = ThingForm()
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "thing_create.html", context)

def thing_update(request, pk):
    thing = Things.objects.get(id=pk)
    form = ThingForm(instance=thing)
    if request.method == "POST":
        form = ThingForm(request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "thing_update.html", context)

def thing_delete(request, pk):
    thing = Things.objects.get(id=pk)
    thing.delete()
    return redirect("/")