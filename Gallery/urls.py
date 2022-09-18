from unicodedata import name
from xml.dom.expatbuilder import DOCUMENT_NODE
from django import views
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [

     path('',views.index, name='index'),
     path('master/',views.master,name='master'),
     path('register/',views.register,name='register'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     path('painting/<slug:data>',views.painting,name='paintingname'),
     path('feedback/',views.feedback,name='feedback'),
     path('imagedetail/<int:pk>',views.imagedetail, name='imagedetail'),
     path('AddToCart/<int:pk>',views.AddToCart,name='AddToCart'),
     path('ViewCart/',views.ViewCart,name='ViewCart'),
     path('increment/<int:id>',views.increment,name='increment'),
     path('decrement/<int:id>',views.decrement,name='decrement'),
     path('remove/<int:id>',views.remove,name='remove'),
     path('customerdetail/',views.Customerdetail.as_view(),name='customerdetail'),
     path('checkout/',views.checkout, name='checkout'),
     path('deleteAdd<int:id>/',views.deleteAdd, name='deleteAdd'),
     path('orderdone/',views.orderdone, name='orderdone'),
     path('errorpage/',views.errorpage,name='errorpage'),
      path('myOrder/',views.myOrder,name='myOrder')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)