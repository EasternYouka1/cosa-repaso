from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate
from .models import Product

def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    
    # Pass products to the template context
    context = {
        'products': products
    }
    
    return render(request, 'products.html', context)


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                             
                return redirect('hola:login')

    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})