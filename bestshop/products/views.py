from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView

from bestshop.products.forms import ProductForm, CommentForm, EditProductForm, RatingsForm
from bestshop.products.models import Product, Purchase

UserModel = get_user_model()
def home(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_products': all_products,
        'page_obj': page_obj,
        'products_count': all_products.count()
    }

    return render(request,'home.html',context)

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
    else:
        form = ProductForm()

    context = {
        'form':form,
    }

    return render(request,'products/add_product.html',context)

def product_details(request,pk):
    product = Product.objects.get(pk=pk)
    curr_user = request.user.pk
    is_rated = len(product.ratings_set.all().filter(user=curr_user)) > 0

    ratings = product.ratings_set.all()
    if ratings:
        avr_rating_price = sum([rate.rating_price for rate in ratings])/len(ratings)
        avr_rating_quality = sum([rate.rating_quality for rate in ratings])/len(ratings)
        avr_rating_design = sum([rate.rating_design for rate in ratings])/len(ratings)
    else:
        avr_rating_price = None
        avr_rating_quality = None
        avr_rating_design = None

    is_owner = product.user == request.user

    context = {
        'product':product,
        'comment_form': CommentForm(
            initial={
                'product_pk': pk,
            }
        ),
        'comments': product.comment_set.all(),
        'is_owner': is_owner,
        'is_rated': is_rated,
        'avr_rating_price': avr_rating_price,
        'avr_rating_design': avr_rating_design,
        'avr_rating_quality': avr_rating_quality
    }

    return render(request,'products/product_details.html',context)

@login_required
def rate_product(request,pk):
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.product_id = pk
            rating.save()
            return redirect('details product', pk)
    else:
        form = RatingsForm()

    context = {
        'form': form,
        'product_pk': pk
    }

    return render(request, 'products/rate_product.html', context)


@login_required
def comment_product(request,pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect('details product', pk)

@login_required
def product_edit(request,pk):
    product = Product.objects.get(pk=pk)

    curr_user = request.user
    product_user = product.user

    if curr_user != product_user:
        return render(request,'products/cant_edit.html')

    if request.method == "POST":
        form = EditProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product.user = request.user
            form.save()
            return redirect('home')

    else:
        form = ProductForm(instance=product)

    context = {
        'form':form,
        'product':product,
    }

    return render(request,'products/edit_product.html',context)

@login_required
def product_delete(request,pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('home')
    else:
        context = {
            'product':product,
        }
        return render(request, 'products/delete_product.html', context)

@login_required()
def buy(request,pk):
    product = Product.objects.get(pk=pk)
    purchase = Purchase()
    purchase.purchase_date = datetime.now()
    purchase.product = product
    purchase.user = request.user

    purchase.save()

    return render(request, 'buy.html')



class ContactListView(ListView):
    paginate_by = 2
    model = Product