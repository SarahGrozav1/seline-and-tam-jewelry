from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Your product was successfully added!')
            return redirect(reverse('products:detail_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'   
    context = {
        'form' : form,
    }
    
    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products:detail_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    
    template = 'products/edit_product.html'   
    context = {
        'form' : form,
        'product' : product,
    }
    
    return render(request, template, context)

def delete_product(request, product_id):
    """ Delete a product from store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:products'))
    