from django.contrib import admin
from .models.Registration_form import registration
from .models.login import Login
from .models.Stock import Stock
from .models.order import Order

# Register your models here.
class AdminRegister(admin.ModelAdmin):
    list_display = ['Name',"Email","Mobile_No"]
    
class AdminStock(admin.ModelAdmin):
    list_display = ['Total_Stock','Total_Sales']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['Name',"Email","Address"]

admin.site.register(registration,AdminRegister)
admin.site.register(Stock)
admin.site.register(Login)
admin.site.register(Order,OrderAdmin )