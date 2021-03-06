from django.shortcuts import render
from .models import Pizza, Topping 

def index(request):
        return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas' : pizzas}
    return render (request, 'pizzas/pizzas.html', context)

def toppings(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.topping_set.order_by()
    context = {'pizza' : pizza, 'toppings' : toppings}
    return render (request, 'pizzas/toppings.html', context)
