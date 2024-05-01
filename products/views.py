from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Collections, ReviewRating, Wishlist
from .forms import ProductForm, ReviewForm
from django.db.models import Avg

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
    review = ReviewRating.objects.filter(product_id=product_id).order_by('-comment')
    
    average = review.aggregate(Avg("rating"))['rating__avg']
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        'reviews': review,
        'product': product,
        'average': average 
    }

    return render(request, 'products/detail_product.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """ 
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home:home'))
    
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


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home:home'))
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


@login_required
def delete_product(request, product_id):
    """ Delete a product from store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home:home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:products'))

@login_required
def submit_review(request, product_id):
    if request.method == 'POST':
       product_id = request.POST.get('product_id') 
       print(product_id)
       product = get_object_or_404(Product, pk=product_id)
       print(product)
       comment = request.POST.get('comment')
       rating = request.POST.get('rating')
       user_profile = request.user.userprofile
       ReviewRating.objects.create(user=user_profile, product=product, comment=comment, rating=rating)
       messages.success(request, 'Your review has been submitted!')
    else:
        messages.error(request, 'Failed to add a review. The stars are required.')
    return redirect('products:detail_product', product_id=product_id)
       
def edit_review(request, product_id, review_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        review = ReviewRating.objects.get(product=product_id, id=review_id)
        
        if request.user == review.user:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    messages.success(request, 'Successfully updated review!')
                    return redirect("products:detail_product", product_id=product_id)
        else:
            form = ReviewForm(instance=review)
            return render(request, 'products/editreview.html', {"form": form})
            

def delete_review(request, product_id, review_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        review = ReviewRating.objects.get(product=product_id, id=review_id)
           
        if request.user == review.user:
            review.delete()
        messages.success(request, 'Your review was deleted!')
        return redirect("products:detail_product", product_id=product_id)
    
# Add to wishlist function

def add_to_wishlist(request, product_id):
    # Retrieve the product object from the database using its id
    product = Product.objects.get(id=product_id)

    # Retrieve the user's wishlist from the database or create a new one if it doesn't exist
    wishlist, created_on = Wishlist.objects.get_or_create(user=request.user)

    # Add the product to the user's wishlist
    wishlist.products.add(product)

    # Redirect the user to the product detail page
    return redirect('products:detail_product', product_id=product_id)

# Wishlist page 

def wishlist(request):
    user_wishlist = Wishlist.objects.filter(user=request.user).first()
    context = {
        'wishlist': user_wishlist
        }
    return render(request, 'products/wishlist.html', context)
