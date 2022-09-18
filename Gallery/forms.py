from django.forms import ModelForm,Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

#class registrationForm(UserCreationForm):
class customerForm(ModelForm):
    class Meta:
        model=Customer
        fields = ('name','city','zipcode','state','address')
        widgets = {
            'address': Textarea(attrs={'cols':23, 'rows':3}),
        }