from django.shortcuts import render

from catalog.models import Product

# Create your views here.
def home(request):
    my_prod = Product.objects.order_by('-id')[0:5]
    print(my_prod)
    return render(request, 'catalog/home.html')



def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')
