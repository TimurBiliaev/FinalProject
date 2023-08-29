from django.shortcuts import render
from GuiShop.models import *
from django.shortcuts import get_object_or_404
from cart.forms import CartAddProductForm
# Create your views here.
def RenderIndex(request, cat_slag):
    if request.method == "POST":
        name_of_product = request.POST.get("searchform")
        images = Gallery.objects.all()
        context = {
            "categories": Category.objects.all,
            "products": Product.objects.filter(name__startswith=name_of_product),
            "images": images
        }
        return render(request, 'index.html', context)
    if cat_slag == "all":
        images = Gallery.objects.all()
        context = {
            "categories": Category.objects.all,
            "products": Product.objects.all,
            "images": images

        }
        return render(request, 'index.html', context)
    else:
        images = Gallery.objects.all()
        category = get_object_or_404(Category, slug=cat_slag)
        products = Product.objects.filter(category=category.id)
        context = {
            "categories": Category.objects.all,
            "products": products,
            "images": images

        }
        return render(request, 'index.html', context)

def RenderProduct(request, post_slug):
    product = get_object_or_404(Product, slug=post_slug)
    cart_product_form = CartAddProductForm()
    context = {'product':product,
               'cart_product_form':cart_product_form,}

    return render(request, 'product.html', context)

def wiew_home(request):
    return RenderIndex(request, 'all')

def Render_aboutus(request):
    pass
