from django.contrib import admin

from .models import pictures,feedback,Customer,cart,oderplace

# Register your models here.

admin.site.register(pictures)
admin.site.register(feedback)
admin.site.register(Customer)
admin.site.register(cart)
admin.site.register(oderplace)


