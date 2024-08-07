from django.shortcuts import render,HttpResponse
from Apna.models import Contact 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product,Cart,Order
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Product,Address
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from django import forms
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator
# @login_required
# def private_place(request):
#     return HttpResponse("Shhh, members only!", content_type="text/plain")




def index(request):
    user=request.user
    is_admin = request.user.groups.filter(name='admin').exists()
    return render(request, 'Apna/index.html',locals())




from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib.auth.hashers import check_password  # To verify hashed passwords
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User  # Necessary for session management
from django.views import View



def login_view(request):
    # print('i login')
    print("POST method ke uper")
    if request.method == 'POST':
        print("POST method ke ander")
        username=request.POST.get('username')
        password=request.POST.get('login_password')
        print(username,password)
        if not User.objects.filter(username=username).exists():
            messages.error(request,"invalid username")
            return render(request, 'Apna/login.html')
        user=authenticate(username=username,password=password)
        print("--------------------",user)
        if user is None:
            messages.error(request,"invalid password")
            return render(request, 'Apna/login.html')

        else:
            login(request,user)
            return render(request, 'Apna/index.html')

    return render(request, 'Apna/login.html')
def logout_page(request):

    logout(request)
      
    request.session.flush()
    
    return render(request,'Apna/index.html')


    
def signup_view(request):
    if request.method== 'POST':
       first_name=request.POST.get("first_name")
       last_name=request.POST.get("last_name")
       username=request.POST.get("username")
       password=request.POST.get("password")

       user=User.objects.filter(username=username)
       if user.exists():
          messages.info(request,"username already taken ")
          return render(request, 'Apna/signup.html')
       user=User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,

       )
       user.set_password(password)
       user.save()
       messages.info(request,"successfully user created")
       return render(request, 'Apna/login.html')
       
    return render(request, 'Apna/signup.html')



class categories_view(View):
    def get(self,request,val):
        product=Product.objects.filter(item_category=val)
        print(product)
        item_name=Product.objects.filter(item_category=val).values('item_name')
        paginator = Paginator(product,5)
        page_number = request.GET.get("page")
        print(page_number)
        
        page_obj = paginator.get_page(page_number)
        invalid_page = False
        if page_number:
            try:
                page_number = int(page_number)
                if page_number < 1 or page_number > paginator.num_pages:
                    invalid_page = True
            except ValueError:
                invalid_page = True
        return render(request, "Apna/categories.html",locals())
        

def categories(request):
    return render(request, 'Apna/categories.html')
       
class brands_view(View):
    def get(self,request,val):
        product=Product.objects.filter(item_brand=val)
        item_name=Product.objects.filter(item_brand=val).values('item_name')
        paginator = Paginator(product,5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        invalid_page = False
        if page_number:
            try:
                page_number = int(page_number)
                if page_number < 1 or page_number > paginator.num_pages:
                    invalid_page = True
            except ValueError:
                invalid_page = True
        return render(request, 'Apna/brands.html',locals())
def brands(request):
    return render(request, 'Apna/brands.html')
def myorders_view(request):
    return render(request, 'Apna/myorders.html')

@allowed_user(allowed_roles=['admin'])
def buynow_view(request):
    user=User.objects.all()
    
    return render(request, 'Apna/buynow.html',{'user':user})  
def allproducts_view(request):
    product=Product.objects.all()
    paginator = Paginator(product, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    invalid_page = False
    if page_number:
        try:
            page_number = int(page_number)
            if page_number < 1 or page_number > paginator.num_pages:
                invalid_page = True
        except ValueError:
                invalid_page = True
    return render(request, "Apna/allproducts.html", locals())
   
def apnasweet_view(request):
    return render(request, 'Apna/apnasweet.html')
def add_to_cart(request):
     user=request.user
     product_id=request.GET.get("prod_id")
     ids=Cart.objects.filter(user=request.user).values('product_id')

    
     if ids.filter(product_id=product_id).exists():
        plus_cart(request)
     else:
        product=Product.objects.get(id=product_id)
        Cart(user=user,product=product).save()
     return redirect("/cart")
    
def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity*p.product.item_price
        amount=amount+value
    totalamount=amount
    return render(request, 'Apna/add_to_cart.html',locals())
def plus_cart(request):
    if request.method=='GET':
       prod_id=request.GET['prod_id']
       c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
       if c.quantity > 20 :
         messages.info(request,"exceed the limit ")
         return render(request, 'Apna/add_to_cart.html')
       c.quantity+=1
       c.save()
       user=request.user
       cart=Cart.objects.filter(user=user)
       amount=0
       for p in cart:
            value=p.quantity*p.product.item_price
            amount=amount+value
       totalamount=amount
       print(prod_id)
       
       data={
        'quantity':c.quantity,
        'amount':amount,
        'totalamount':totalamount
       }
       return JsonResponse(data)

def minus_cart(request):
    if request.method=='GET':
       prod_id=request.GET['prod_id']
       c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
       c.quantity-=1
       c.save()
       user=request.user
       cart=Cart.objects.filter(user=user)
       amount=0
       for p in cart:
            value=p.quantity*p.product.item_price
            amount=amount+value
       totalamount=amount
       print(prod_id)
     
       data={
        'quantity':c.quantity,
        'amount':amount,
        'totalamount':totalamount
       }
       return JsonResponse(data) 
def remove_cart(request):
    if request.method=='GET':
       prod_id=request.GET['prod_id']
       c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
       c.delete()
       user=request.user
       cart=Cart.objects.filter(user=user)
       amount=0
       for p in cart:
            value=p.quantity*p.product.item_price
            amount=amount+value
       totalamount=amount
       print(prod_id) 
       data={
        'quantity':c.quantity,
        'amount':amount,
        'totalamount':totalamount
       }
       return JsonResponse(data) 
def remove_add(request):
        choice=request.GET.get("add")
        print(choice)
        print(choice)
        address = get_object_or_404(Address, id=choice)
        address.delete() 
        return render(request,'Apna/checkout.html')
           
    # if request.method=='GET':
       
    #     choice=request.GET.get("add")
    #     print(choice)
    #     a=Address.objects.filter(id=choice)
    #     print(a)
        
    #     a.delete()
        # user=request.user    
       
       
    
# def add_address(request):
#      if request.method=="GET":
#         address=request.GET.get("address")
#         address2=request.GET.get("address2")
#         city=request.GET.get("city")
#         state=request.GET.get("state")
#         zips=request.GET.get("zip")
#         u=Address.objects.filter(user=request.user)
#         print(u)
#         add=Address.objects.create(
#             address=address,
#             adress_2=address2,
#             city=city,
#             state=state,
#             zip=zips,
#             user=request.user,
#         )
#         add.save()
#      return render(request, 'Apna/checkout.html')
    
       

def checkout(request):
        if request.method=="GET":
            user=request.user
            cart_items=Cart.objects.filter(user=user)
            amount=0
            for p in cart_items:
                value=p.quantity*p.product.item_price
                amount=amount+value
            totalamount=amount
            print(request.GET)
            u=Address.objects.filter(user=request.user)
            print("GET")
            print(u)
            add_address=request.GET.get("add_address")
            print(add_address)
            deletes=request.GET.get("delete1")
            print(deletes)
            choice=request.GET.get("add")
            print(choice)
            counts=u.count()
            if deletes:
                print("uoui")
                s= Address.objects.filter(id=choice ,user=request.user)
                print(s)
                s.delete()
                return redirect("g")
            
            # if delete:
            #      print("in delete")   
            #      s= Address.objects.filter(id=choice)
            #      print(s)
            #      s.delete()


        if request.method=="POST":
            print(request.POST)


            address=request.POST.get("address")
            address2=request.POST.get("address2")
            city=request.POST.get("city")
            state=request.POST.get("state")
            zips=request.POST.get("zip")
            deletes=request.POST.get("delete1")
            print(address)
            print(address2)
            choice=request.POST.get("add")
            print(choice)
            u=Address.objects.filter(user=request.user)
            print(u)
            print(u.count())
            counts=u.count()
            
            
            if u:
                if u.count()<=5:
                    print("in the u ")
                    add_address=request.POST.get("add_address")
                    print(add_address)
                    # ord=Order.objects.create(
                    #     address_id=address,
                    #     )
                    # ord.save()
                    
                    if add_address :
                        if not Address.objects.filter(user=request.user,adress_2=address2,address=address, city=city, state=state,zip=zips).exists():
                            print(Address.objects.filter(user=request.user,adress_2=address2,address=address, city=city, state=state,zip=zips))
                            print("add_address")
                            add=Address.objects.create( 
                            address=address,
                            adress_2=address2,
                            city=city,
                            state=state,
                            zip=zips,
                            user=request.user,
                            )
                            add.save()
                            
                            messages.info(request,"successfully user created")
                    if deletes:
                        print("uoui")
                        s= Address.objects.filter(id=choice ,user=request.user)
                        print(s)
                        s.delete()
                        return redirect("g")
                            
                    
                    print("kkk")
                    # if delete:
                    #    print("in delete")   
                    #    s= Address.objects.filter(id=choice)
                    #    print(s)
                    #    s.delete()


                
            else:
                print("out")
                if address:
                    add=Address.objects.create(
                            address=address,
                            adress_2=address2,
                            city=city,
                            state=state,
                            zip=zips,
                            user=request.user,
                    )
                    add.save()
                    print("hello")
                    messages.info(request,"successfully user created")
        user=request.user
        cart_items=Cart.objects.filter(user=user)
        amount=0
        for p in cart_items:
            value=p.quantity*p.product.item_price
            amount=amount+value
        totalamount=amount

        return render(request,'Apna/checkout.html',locals())
def searchbar_view(request):
    if request.method=='GET':
        query=request.GET.get("q")
        product=Product.objects.all().filter(item_name__icontains=query)
        return render(request, 'Apna/search.html',{'product':product})
    else:
        return HttpResponse("no result found")

    return render(request,'Apna/index.html')

def clear_cart(request):
    if request.method=="GET":
        user_cart =Cart.objects.filter(user=request.user)
        user_cart.delete()  # This method should clear the cart items
        messages.info(request,"successfully")   
    
    return render(request,'Apna/index.html') 
# Create your views here.
# from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(lambda user: user.is_staff)
# def staff_place(request):
#     return HttpResponse("Employees must wash hands", content_type="text/plain")
def g(request):
    return render(request,'Apna/receipt.html',locals()) 
def receipt(request):
    if request.method=='GET':
        delete1=request.GET.get("delete1")
        choice=request.GET.get("add")
        print(delete1)
        if delete1:
            print("uoui")
            s= Address.objects.filter(id=choice ,user=request.user)
            print(s)
            s.delete()
            return redirect("g")


       
        user=request.user
        cart_items=Cart.objects.filter(user=user)
        amount=0
        for p in cart_items:
            value=p.quantity*p.product.item_price
            amount=amount+value
        totalamount=amount
        u=Address.objects.filter(user=request.user)
        choice=request.GET.get("add")
        print(choice)
        a=Address.objects.filter(id=choice)
           
    return render(request,"Apna/receipt.html",locals())
