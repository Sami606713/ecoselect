from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.db import transaction
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from products.models import Products,Contact,Address,ProductImage,Order
import math,os
from bson import ObjectId
from products.utils import fetch_product
# Api imports
from rest_framework import viewsets
from rest_framework import permissions
from products.models import Products
from products.serializers import ProductSerializer
# costom log-in imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Stipe
import stripe
from django.conf import settings
import json

# Create your views here.
# Api end points class
class ProductViewsets(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # Fetch the data
    def get_data(self,id):
        try:
            return Product.object.get(pk=id)
        except:
            raise HttpResponse("<h1>Id not found</h1>")

# End of API

# products end point
def index(request):
    # print(fetch_product())
    # fetch all the product
    product=Products.objects.all()

    # based on product fetch the images
    prod_img=ProductImage.objects.filter(product__in=product)

    # makea  empty dict
    img_dic={}
    for img in prod_img:
        if(img.product_id not in img_dic):
            img_dic[img.product_id]=img.image.url
    # print(set(img_dic.values()))
    # Nbr od slides we want to display
    n=len(product)
    nbr_of_slides=n//4 + math.ceil((n/4)-(n//4))
    # For displaying the image
   
    params={"product":product,"Nbr of slides":nbr_of_slides,"range":range(nbr_of_slides),"img_dic":img_dic}
    return render(request,"index.html",params)


def contact(request):
    # addres=Address.objects.all()
    # order=Order.objects.filter(address__in=addres)
    # img_dic={}
    # for img in order:
    #     if(img.order_id not in img_dic):
    #         # img_dic[img.product_id]=img.image.url
    #         print()
    if(request.method=="POST"):
        name=request.POST.get("name")
        phone_nbr=request.POST.get("phone_number")
        email=request.POST.get("email")
        msg=request.POST.get("message")
        print(name,phone_nbr,email,msg)

        contact=Contact(name=name,email=email,phone=phone_nbr,msg=msg)
        contact.save()
        # send_email(name=name,phone_nbr=phone_nbr,email=email,msg=msg)

    return render(request,"contact.html")


def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request,"about.html")

def signup(request):
    if(request.method=="POST"):
        user_name=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        # confirm_pass=request.POST.get("pass")

        new_user=User.objects.create_user(user_name,email,password)
        new_user.save()
        return redirect("log_in")
    return render(request,"registration/signup2.html")


def log_in(request):
    if (request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        # print(user)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("/product/log_in")
    return render(request,"registration/log_in.html")

def log_out(request):
    logout(request)
    return redirect("/")
# Product view
def product_view(request,id):
    # fetch the item
    product=Products.objects.filter(pk=id)
    # fetch the item image
    prod_image=ProductImage.objects.filter(product__in=product)
    # Fetch  the image url
    img_url=[image.image.url for image in prod_image]
    # print(img_url)
    
    return render(request,"product_view.html",{"fetch_product":product[0],"image_url":img_url})

# Cart 
def cart(request):
    return render(request, "shoping_cart.html")

# address
@transaction.atomic
def address(request):
    if(request.method=="POST"):
        item=request.POST.get("itemjson")
        name=request.POST.get("name")
        phone_nbr=request.POST.get("nbr")
        address=request.POST.get("addr")
        code=request.POST.get("code")
        email=request.POST.get("email")
        province=request.POST.get("province")
        city=request.POST.get("city")
        area=request.POST.get("area")

        # print("         ",name)
        new_address=Address(
            name=name,
            province=province,
            code=code,
            area=area,
            city=city,
            email=email,
            mobile=phone_nbr,
            address=address
        )

        # print("         ",item)
        new_address.save()
        new_order = Order(item_json=item, address=new_address)
        new_order.save()
        return redirect("order")
    return render(request,"address.html")

# order 
def order(request):
    if(request.method=="POST"):
         # Order item
        item=request.POST.get("itemjson")
        # new_order=Order(item_json=item)
        # new_order.save()
    return render(request,"order.html")
# end order


def product_filter(request):
    if(request.method=="POST"):
        cate=request.POST.get("category")
        # product=Products.objects.all()
        # filter product
        filter_product=Products.objects.filter(category=cate)

        # filter product images
        product_image=ProductImage.objects.filter(product__in=filter_product)
        # print(product_image)
        # print(cate,product)
        img_dic={}

        for image in product_image:
            if(image.product_id not in img_dic):
                print(image.image.url)
                img_dic[image.product_id]=image.image.url
            # print(image)
        parms={"filter":filter_product,"img_url":img_dic}

        
    # return HttpResponse("Filter page")
    return render(request,"product_filter.html",parms)

  


# Stipe payment
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create a PaymentIntent
            payment_intent = stripe.PaymentIntent.create(
                amount=1000000,
                currency='PKR',
                # Additional parameters as needed
            )

            checkout_session = stripe.checkout.Session.create(
                # success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                 success_url=domain_url + '/product/success/',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=fetch_product()
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def success(request):
    session_id = request.GET.get('session_id')
    try:
        # Retrieve the Checkout Session to check the payment status
        checkout_session = stripe.checkout.Session.retrieve(session_id)

        # Handle the success scenario based on the payment status
        if checkout_session.payment_status == 'paid':
            # Payment is successful
            return render(request, 'success.html', {'session_id': session_id})
        else:
            # Payment is not successful
            return render(request, 'failure.html', {'session_id': session_id, 'error_message': 'Payment failed.'})
    except stripe.error.StripeError as e:
        # Log the error for debugging purposes
        print(f"Stripe error: {str(e)}")
        return render(request, 'success.html', {'session_id': session_id, 'error_message': 'Payment failed. Please try again.'})
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {str(e)}")
        return HttpResponse(f'Error: {str(e)}')