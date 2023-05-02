from django.urls import path
from . import views

urlpatterns = [
    path("/error", views.show_error, name="error page")
]
