from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import list_item
from .forms import ItemForm


# Create your views here.

def home(request):
    
    return render(request, 'main/home.html')

def items(request):
    items = list_item.objects.all()
    context = {"items":items}
    return render(request, "main/list.html", context)


class itemCreate(CreateView):
    model = list_item
    template_name = "main/create_item.html"
    form_class = ItemForm
    success_url = "list/"
    
class itemUpdate(UpdateView):
    model = list_item
    template_name = "main/update_item.html"
    form_class = ItemForm
    success_url = "/item/list/"
    
class itemDelete(DeleteView):
    model = list_item
    template_name = "main/delete_item.html"
    success_url = "/item/list/"