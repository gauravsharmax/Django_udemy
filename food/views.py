from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import Itemform
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    
    context = { 
        'item_list' : item_list
    }
    return render(request,"food/index.html",context)

def item(request):
    return HttpResponse("<h1>This is an Item Page.</h1>")

def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item" : item,
    }
    return render(request,"food/details.html",context)


def create_item(request):
    if request.method == "POST":
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = Itemform()
    return render(
        request,
        'food/item-form.html',
        {
            "form": form
        }
    )
    # print(form.errors)

    # if form.is_valid():
    form.save()
    return redirect('food:index')
    
    
    # return render(request,'food/item-form.html',{'form':form})
