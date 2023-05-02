from django.shortcuts import render

# Create your views here.


def show_error(request):
    return render(request, "error_page.html")
