from account.models import Cart,Order

def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
        order = Order.objects.filter(user=request.user).count()
        return {'cart':count , 'order':order}
    else:
        return {'cart':0 , 'order':0}
    
    