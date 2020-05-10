from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import Registerform

# Create your views here.

class ProductList(ListView):
  model = Product
  template_name = 'product.html'
  context_object_name = 'product_list' # attribute name 설정 > 안할시 object_list

class ProductCreate(FormView):
  template_name = 'register_product.html'
  form_class = Registerform
  success_url = '/product/'

class ProductDetail(DetailView):
  template_name = 'product_detail.html'
  queryset = Product.objects.all() # 추후 filter통해 보여줄것들만 걸러낼수도있음
  context_object_name = 'product' #실제 탬플릿에서 사용할 변수명
