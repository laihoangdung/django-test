from django.shortcuts import render
from .models import Product
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from .forms import CreateProductForm
from django.shortcuts import redirect

# Create your views here.
def get_all_products(request):
    products = Product.objects.all().order_by("id")
    # template = loader.get_template("product/product.html")
    context = {
        "products": products
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "product/list.html", context)


def get_product_details(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product does not exists")
    return render(request, "product/details.html", {"product": product})


def create_product(request):
    form = CreateProductForm()

    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = Product.objects.create(
                title=form.cleaned_data["title"],
                desc=form.cleaned_data["desc"],
                price=form.cleaned_data["price"],
            )
            print(product)
            return redirect("/my-product")

    return render(request, "product/create.html", {"form": form})
