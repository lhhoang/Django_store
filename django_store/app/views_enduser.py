from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from datetime import datetime

priceRangeList = [
    {'id': 1, 'max': 10*1000000},
    {'id': 2, 'min': 10*1000000, 'max': 20*1000000},
    {'id': 3, 'min': 20*1000000}
]


def index(request):
    data = request.GET
    name = data.get('name', '')

    categoryId = data.get('categoryId', '')
    categoryId = int(categoryId) if categoryId.isdigit() else None

    priceRangeId = data.get('priceRangeId', '')
    priceRangeId = int(priceRangeId) if priceRangeId.isdigit() else None

    productList = Product.objects.all()
    if name:
        productList = productList.filter(name__icontains=name)

    if categoryId:
        productList = productList.filter(category__id=categoryId)

    if priceRangeId and priceRangeId <= len(priceRangeList):
        priceRange = priceRangeList[priceRangeId-1]
        minPrice = priceRange.get('min')
        maxPrice = priceRange.get('max')

        if minPrice:
            productList = productList.filter(price__gte=minPrice)

        if maxPrice:
            productList = productList.filter(price__lte=maxPrice)

    categoryList = Category.objects.all()
    context = {
        'name': name,
        'categoryId': categoryId,
        'priceRangeId': priceRangeId,
        'productList': productList,
        'categoryList': categoryList,
        'priceRangeList': priceRangeList
    }
    return render(request, 'enduser/index.html', context)


def viewProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'enduser/view_product.html', context)


def orderProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = OrderForm(initial={'qty': 1})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order()
            order.product = product
            order.qty = int(data.get('qty'))
            order.priceUnit = product.price
            order.total = order.qty * order.priceUnit
            order.customerName = data.get('customerName')
            order.customerPhone = data.get('customerPhone')
            order.customerAddress = data.get('customerAddress')
            order.orderDate = datetime.now()
            order.status = Order.Status.PENDING
            order.save()

    context = {'form': form, 'product': product}
    return render(request, 'enduser/order_product.html', context)


def thankYou(request):
    return render(request, 'enduser/thank_you.html')
