from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    #get the cart
    cart=Cart(request)
    cart_products = cart.get_prods
    quantities=cart.get_quants
    totals=cart.cart_total()
    return render(request, 'cart_summary.html', {"cart_products":cart_products,'quantities':quantities,'totals':totals})

def cart_add(request):
    if request.method == 'POST':
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            product_id = request.POST.get('product_id')
            product_qty = request.POST.get('product_qty')

            if product_id is None:
                return JsonResponse({'error': 'No product ID provided'}, status=400)

            product_id = int(product_id)  # Safe to convert
            product_qty = int(product_qty)
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product,quantity=product_qty)

            #get cart quantity
            cart_quantity = cart.__len__()

            # response = JsonResponse({'Product Name': product.name})
            response = JsonResponse({'qty': cart_quantity})
            messages.success(request,('Product added to cart'))
            return response

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        #call delete function in cart
        cart.delete(product=product_id)

        response= JsonResponse({'product':product_id})

        messages.success(request,('Item deleted from shopping cart'))

        return response

    

def cart_update(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id,quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        messages.success(request,('Your cart has been updated'))
        return response
