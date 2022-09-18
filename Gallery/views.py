from ast import Return
from pickle import NONE
import re
from django import template
from django.views.generic.detail import DetailView
from django.views import View 
from django.shortcuts import redirect, render
from .models import feedback, oderplace, pictures,Customer,cart
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import customerForm


#index page
def index(request):
    all=pictures.objects.all()
    return render(request,'index.html',{'all':all})

def master(request):
    return render(request,'master.html')

def register(request):

    if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('pass')
            if User.objects.filter(username=username).exists():
                 return redirect('errorpage')
            data=User.objects.create_user(username=username,email=email,password=password)
            data.save()
            return redirect('login')
    return render(request,'register.html')

def login(request):
   if request.method == 'POST':
      username1 = request.POST.get('username')
      password1 = request.POST.get('pass')
      #check user is valid or note
      user = auth.authenticate(username=username1, password=password1)
      if user is not None:
         auth.login(request,user)
         return redirect('index')
      else:
         messages.error(request,'Enter valid Detail')
         print('invalid')
   return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

#check String(data) passed with url extract value accoding it and pass  
def painting(request ,data="none"):
    paint='None'
    if data=='none':
        paint=pictures.objects.all()
    elif data=='oil':
        paint=pictures.objects.filter(category='p1')
    elif data=='water':
        paint=pictures.objects.filter(category='p2')
    else:
        paint=pictures.objects.filter(category='p3')
    return render(request,'painting.html',{'paint':paint})

#when user click on particular image fetch id and extract
def imagedetail(request,pk):
    user=request.user
    img=pictures.objects.get(id=pk)
    #chek if picture already in cart then display view cart otherwise display addtoadd 
    already_cart=False
    if user.is_authenticated:
        if cart.objects.filter(user=user,picture=img):
            already_cart=True
            print(already_cart)
    return render(request,'pictures_detail.html',{'img':img,'already_cart':already_cart})

def AddToCart(request,pk):
        user=request.user
        if pk==0:
            return redirect('ViewCart')
            
        if  user.is_authenticated:
            user=request.user
            data= pictures.objects.get(pk=pk)
            mycart=cart.objects.create(user=user,picture=data)
            mycart.save()
            return redirect('ViewCart')
        else:
            return redirect('login') 

#calculation of Cart
def ViewCart(request):
    if request.user.is_authenticated:
        user=request.user
        mycart=cart.objects.filter(user=user)

        amount=0.0
        shipping=70.0
        total=0.0
        item=0
        cartitem=[p for p in cart.objects.all() if p.user==user]
        if cartitem:
            for i in cartitem:
                item+=1
                tempamount=i.quantity * i.picture.price 
                amount+=tempamount
                total=amount+shipping
    return render(request,'cart.html', {'carts':mycart ,'total': total ,'amount':amount, 'item':item})

#increment Quntity of picture 
def increment(request,id):
        item=cart.objects.get(pk=id)
        item.quantity+=1
        item.save()
        return redirect('ViewCart')
    
#Decrement Quntity of picture 
def decrement(request,id):
        item=cart.objects.get(pk=id)
        item.quantity-=1
        print(item.quantity)
        item.save()
        return redirect('ViewCart')

#Remove picture from Cart
def remove(request,id):
    item=cart.objects.get(pk=id).delete()
    return redirect('ViewCart')

def feedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        data=feedback.objects.create(name=name,email=email,subject=subject,message=message)        
        data.save()
    return render(request,'contactUs.html')


class Customerdetail(View):
    def get(self,request):
        form=customerForm()
        return render(request,'customer.html',{'form':form})
    def post(self,request):
        form=customerForm(request.POST)  
        return render(request,'checkout.html') 
        

def checkout(request):
    if request.method=='POST':
        form=customerForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            address=form.cleaned_data['address']
            data=Customer.objects.create(user=user,name=name,city=city,zipcode=zipcode,state=state,address=address)
            data.save() 

    user=request.user
    address=Customer.objects.filter(user=user) 
    items=cart.objects.filter(user=user)
    mycart=cart.objects.filter(user=user)

    amount=0.0
    shipping=70.0
    total=0.0
    item=0
    tempamount=0    
    cartitem=[p for p in cart.objects.all() if p.user==user]
    if cartitem:
    
        for i in cartitem:    
            tempamount=i.quantity * i.picture.price 
            amount+=tempamount  
            total=amount+shipping 
            item= item+1
    return render(request,'checkout.html',{'address':address ,'total':total,'temp':tempamount,'cart':mycart, 'item':items} )

# delete address from detail page..
def deleteAdd(request,id):
    add=Customer.objects.get(pk=id).delete()
    return redirect('checkout')

#too save data in orderplaced table
def orderdone(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cartitem=cart.objects.filter(user=user)
    for i in cartitem:
        oderplace(user=user, Customer=customer,pictures=i.picture, quantity=i.quantity).save()
        i.delete()
    order=oderplace.objects.filter(user=user)
    return render(request,'Myorder.html',{'order':order})


def errorpage(request):
    return render(request,'errorpage.html')        

def myOrder(request):
    user=request.user
    order=oderplace.objects.filter(user=user)
    return render(request,'Myorder.html',{'order':order})
