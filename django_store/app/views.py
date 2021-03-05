import json
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html')

# Category


def listCategory(request):
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'staff/category/list.html', context)


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'


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


def listProduct(request):
    return render(request, 'staff/product/list.html')


def createProduct(request):
    return render(request, 'staff/product/form.html')


def updateProduct(request, pk):
    return render(request, 'staff/product/form.html')


# Order

def listOrder(request):
    return render(request, 'staff/order/list.html')


def viewOrder(request, pk):
    return render(request, 'staff/order/view_detail.html')
