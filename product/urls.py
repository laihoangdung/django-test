from django.urls import path

from . import views

app_name = "Products"
urlpatterns = [
    path("", views.get_all_products, name="get_all_products"),
    path("<int:id>/", views.get_product_details, name="get_product_details"),
    path("create/", views.create_product, name="create_product"),
]