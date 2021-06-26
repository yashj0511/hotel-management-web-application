from django.contrib import admin
from . models import customer,order,Table,menu,reservation,waiter,payment

# Register your models here.
admin.site.register(customer)
admin.site.register(order)
admin.site.register(Table)
admin.site.register(menu)

admin.site.register(reservation)
admin.site.register(waiter)
admin.site.register(payment)
