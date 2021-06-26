from django import forms
from django.forms import ModelForm
from .models import customer,order,Table,menu,reservation,waiter,payment





class customer_form(ModelForm):
    class Meta:
        model = customer
        fields='__all__'
        widgets = {
            'Gender':forms.TextInput(attrs={'placeholder':'M-male,F-Female,O-other'}),

        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['ContactNumber'] = forms.BigIntegerField(max_value=9999999999,min_value=1000000000)        





class order_form(ModelForm):
    class Meta:
        model = order
        fields='__all__'


# customer,order,Table,menu,reservation,waiter,payment

# class cuform(forms):

class table_form(ModelForm):
    class Meta:
        model = Table
        fields='__all__'



class menu_form(ModelForm):
    class Meta:
        model = menu
        fields='__all__'      


class reservation_form(ModelForm):
    class Meta:
        model = reservation
        fields='__all__'      

    widgets = {
            'R_time':forms.TextInput(attrs={'placeholder':'mm/dd/yy'}),

        }            


class waiter_form(ModelForm):
    class Meta:
        model=waiter
        fields='__all__'

    widgets = {
            'Gender':forms.TextInput(attrs={'placeholder':'M-male,F-Female,O-other'}),

        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['mobile'] = forms.BigIntegerField(max_value=9999999999,min_value=1000000000)      
            



class payment_form(ModelForm):
    class Meta:
        model=payment
        fields='__all__'
                                