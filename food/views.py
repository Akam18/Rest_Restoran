from django.shortcuts import render
from models import Category, Menu, Events

# Create your views here.

def indexView(request):
    foods = Menu.objects.filter(category__id=id)

    print(foods)
    categories = Category.objects.all()
    events = Events.objects.all()

    context = {
        'foods': foods,
        'categories': categories,
        'events': events,
    }

    return render(request, 'index.html', context)