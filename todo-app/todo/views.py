from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


# Create your views here.
def main(request):
    """The home page for the to-do app"""

    item_list = Todo.objects.order_by("-date")

    if request.method != "POST":
        # No data submitted; create a blank form
        form = TodoForm()
    else:
        # POST data submitted; process data
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:main')

    context = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'index.html', context=context)


def remove(request, id):
    """delete a specific entry"""
    item = Todo.objects.get(pk=id)
    item.delete()
    messages.info(request, "item removed !")
    return redirect('todo:main')
