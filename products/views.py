from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Category, Collections
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products """
    
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    collections = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)
        
        if 'category' in request.GET:
            categories = request.GET['category']
            products = Product.objects.filter(category__name=categories)
            categories = Category.objects.filter(name=categories)
            
        if 'collections' in request.GET:
            collections = request.GET['collections']
            products = Product.objects.filter(collections__name=collections)
            collections = Collections.objects.filter(name=collections)
    
    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products' : products,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_collections': collections,
    }

    return render(request, 'products/products.html', context)
    

def detail_product(request, product_id):
    """ A view to show the detail of an product """
    
    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product' : product,
    }

    return render(request, 'products/detail_product.html', context)

def add_product(request):
    """ Add a product to the store """ 
    form = ProductForm()
    template = 'products/add_product.html'   
    context = {
        'form' : form,
    }
    
    return render(request, template, context)