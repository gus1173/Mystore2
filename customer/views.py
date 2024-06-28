from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from account.models import Products,Cart,Order
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

def sign_in_required(fn):
    def inner(request,*ar,**kw):
        if request.user.is_authenticated:
            return fn(request,*ar,**kw)
        else:
            messages.info(request,'Login First!!')
            return redirect('logout')
    return inner

decor=[never_cache,sign_in_required]

@method_decorator(decor,name='dispatch')
class indexview(ListView):
    template_name='customerhome.html'
    queryset = Products.objects.all()
    context_object_name ='products'

@method_decorator(decor,name='dispatch')
class detailview(DetailView):
    template_name='det.html'
    queryset = Products.objects.all()
    context_object_name ='products'
    pk_url_kwarg='id'

decor
def addtocart(request,*a,**kw):
    pid=kw.get('id')
    product=Products.objects.get(id=pid)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,products=product)
        messages.info(request,'Already Added to cart')
        return redirect ('index')
    except:
        Cart.objects.create(user=user,products=product)
        messages.success(request,'Added to cart')
        return redirect ('index')

@method_decorator(decor,name='dispatch')
class CartView(ListView):
    template_name='cart.html'
    queryset = Cart.objects.all()
    context_object_name ='cartitems'
    def get_queryset(self):
        qs=  super().get_queryset()
        qs=  qs.filter(user=self.request.user)
        return qs
    
def RemoveCartItem(request,*ar,**kw):
    Cart.objects.get(id=kw.get('id')).delete()
    messages.success(request,'Removed from cart!!')
    return redirect('cartview')

@method_decorator(decor,name='dispatch')
class CheckoutView(TemplateView):
    template_name='order.html'
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        cart = Cart.objects.get(id=kwargs.get('id'))
        context['product'] = cart.products
        return context
    def post(self,request,*ar,**kw):
        cart = Cart.objects.get(id=kw.get('id'))
        prod =cart.products
        user=request.user
        phn = request.POST.get('phone')
        adr = request.POST.get('address')
        Order.objects.create(user=user,products=prod,phone=phn,address=adr)
        cart.delete()
        return redirect('cartview')
  
@method_decorator(decor,name='dispatch')  
class OrdersListView(ListView):
    template_name='orderslist.html'
    queryset = Order.objects.all()
    context_object_name ='orders'
    def get_queryset(self):
        qs =  super().get_queryset()
        qs =  qs.filter(user=self.request.user)
        return qs
    
decor  
def CancelOrder(request,*ar,**kw):
    Order.objects.get(id=kw.get('id')).delete()
    messages.success(request,'Order Cancelled!!')
    return redirect('orderlist')
