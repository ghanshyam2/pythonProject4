from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def index(request):
    item_list = ToDoModel.objects.order_by("-created")
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ToDoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)


def remove(request, item_id):
    item = ToDoModel.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('/')
