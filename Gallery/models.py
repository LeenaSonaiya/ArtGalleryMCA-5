from distutils.command.upload import upload
import email
from email import message
from sqlite3 import Cursor
from sre_constants import CATEGORY
from statistics import quantiles
from telnetlib import STATUS
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY=(('p1','oil painting'),
            ('p2','Watercolor painting '),
            ('p3','spay painting')
            )

class pictures(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    desc=models.TextField()
    category=models.CharField(choices=CATEGORY,max_length=5)
    image=models.ImageField(upload_to= 'picimage')

    def __str__(self):
            return str(self.title)

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    picture=models.ForeignKey(pictures,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.user)

    @property
    def total_cost(self):
      return  self.quantity * self.picture.price
    

State=(('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'))


class Customer(models.Model):
   
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(choices=State,max_length=200)
    zipcode=models.IntegerField()
    address=models.CharField(max_length=200)
    

    def __str__(self):
        return str(self.name)

Status=(('Accepted','Accepted'),
        ('On the Way','On the way'),
        ('Delivered','Deliverd'),
        ('Cancle','Cancle')
    )

class oderplace(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    pictures=models.ForeignKey(pictures,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=Status,default='Pending',max_length=200)

    def __str__(self):
            return str(self.Customer) 

class feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
            return (self.name)  