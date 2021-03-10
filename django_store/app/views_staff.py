import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html')

# Category


@login_required
def listCategory(request):
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'staff/category/list.html', context)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'


@login_required
def deleteCategory(request, pk):
    error = ''
    success = False
    if request.method == 'POST':
        try:
            c = Category.objects.get(pk=pk)
            c.delete()
            success = True
        except Exception as e:
            error = str(e)
    else:
        error = 'Method not allow'
    result = {'success': success, 'error': error}
    return HttpResponse(json.dumps(result), content_type='application/json')
# Product


@login_required
def listProduct(request):
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request, 'staff/product/list.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'staff/product/form.html'
    success_url = '/staff/list-product'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'staff/product/form.html'
    success_url = '/staff/list-product'


@login_required
def deleteProduct(request, pk):
    error = ''
    success = False
    if request.method == 'POST':
        try:
            p = Product.objects.get(pk=pk)
            p.delete()
            success = True
        except Exception as e:
            error = str(e)
    else:
        error = 'Method not allow'
    result = {'success': success, 'error': error}
    return HttpResponse(json.dumps(result), content_type='application/json')
# Order


@login_required
def listOrder(request):
    orderList = Order.objects.all()
    context = {'orderList': orderList}
    return render(request, 'staff/order/list.html', context)



@login_required
def viewOrder(request, pk):
    order =get_object_or_404(Order, pk=pk)
    context = {'order': order}
    return render(request, 'staff/order/view_detail.html', context)

@login_required
def confirmOrderDelivered(request, pk):
    error = ''
    success = False
    if request.method == 'POST':
        try:
            order = get_object_or_404(Order, pk=pk)
            order.status = Order.Status.DELIVERED
            order.deliverDate = datetime.now()
            order.save()
            success = True
        except Exception as e:
            error = str(e)
    else:
        error = 'Method not allow'
    result = {'success': success, 'error': error}
    return HttpResponse(json.dumps(result), content_type='application/json')

@login_required
def cancelOrder(request, pk):
    error = ''
    success = False
    if request.method == 'POST':
        try:
            order = get_object_or_404(Order, pk=pk)
            order.status = Order.Status.CANCELLED
            order.save()
            success = True
        except Exception as e:
            error = str(e)
    else:
        error = 'Method not allow'
    result = {'success': success, 'error': error}
    return HttpResponse(json.dumps(result), content_type='application/json')