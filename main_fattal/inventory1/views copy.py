from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StockCreateForm, SuppliersCreateForm, StockSearchForm,StockUpdateForm, StockFullSearchForm
from .models import *
from datetime import datetime
# Create your views here.


def homepage_view(request):
    #this is the title for now
    #print (request.user)
  
    today = datetime.now().date()
    context= {
     
        "today": today,
        
    }
    #return HttpResponse('<h1>Avi S. onlyavi@gmail.com</h1>')
    return render(request,"home.html", context) #instead of context {} empty dic
"""  """



def about_view(request):
    title='Welcome to my first Django project'
    today = datetime.now().date()
    aboutmyself= "My name is Avi Sivan. My email onlyavi@gmail.com"
    context= {
        "title":title,
        "today": today,
        "aboutmyself":aboutmyself
        
    }
    
    return render(request, "about.html",context)


def under_construction(request):
   
    return render(request, "under_construction.html")

def add_newitem_view(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    context ={
        "form":form,
        "title":"Add New Item",
        
    }
    return render(request, "add_newitem.html", context)

def update_items(request,pk):
    #pk is the object we want to update
    queryset= Stock.objects.get(id=pk)
    form=StockUpdateForm(instance=queryset)
    if request.method=='POST':
        form=StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    context={
        "form":form,
        
    }
    return render(request, 'add_newitem.html',context)       
"""  """


def list_items_view(request):
    header ='List of items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context ={
        "header": header,
        "queryset":queryset,
        "form": form,
                          
    }
#    fields_full=['category_name','item_name','item_fattal_code','item_barcode_external',
# 'quantity_item', 'description']
        
        
    if request.method == 'POST':
        queryset = Stock.objects.filter(category_name__icontains=form['category_name'].value(),
                                        item_name__icontains=form['item_name'].value(),
                                        quantity_item__icontains=form['quantity_item'].value(),
                                        item_fattal_code__icontains=form['item_fattal_code'].value(),
                                        item_unit_kind__icontains=form['item_unit_kind '].value(),
                                        description__icontains=form['description'].value(),
                                        
                                        
        )
    
        
    context ={
        "form": form,
        "header": header,
        "queryset": queryset,
      
                
    }
    
    
    return render(request, "list_items.html", context)



def StockFSearch_view(request):
    header ='Full Item Search'
    form = StockFullSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context ={
        "header": header,
        "queryset":queryset,
        "form": form,
                          
    }
#    fields_full=['category_name','item_name','item_fattal_code','item_barcode_external',
# 'quantity_item', 'description']
        
        
    if request.method == 'POST':
        queryset = Stock.objects.filter(category_name__icontains=form['category_name'].value(),
                                        item_name__icontains=form['item_name'].value(),
                                        quantity_item__icontains=form['quantity_item'].value(),
                                        item_fattal_code__icontains=form['item_fattal_code'].value(),
                                        item_unit_kind__icontains=form['item_unit_kind '].value(),
                                        description__icontains=form['description'].value(),
                                        
                                        
        )
    
        
    context ={
        "form": form,
        "header": header,
        "queryset": queryset,
                
    }
    
    
    return render(request, "full_search.html", context)

def delete_items(request,pk):
    #instance = get_object_or_404( id=pk)
    instance = Stock.objects.get(id=pk)
    instance.delete()
    return redirect('/')




    
