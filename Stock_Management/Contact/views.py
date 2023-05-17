from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.Registration_form import registration
from .models.login import Login
from .models.Stock import Stock
from .models.order import Order
# Create your views here.



def Registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            
            register = registration(Name = name,Email = email,Mobile_No =mobile,Password =password ,Confirm_password = confirm )
            register.save()
        else:
            return HttpResponse("Dont'write different password")
    return render(request,"Registration.html")

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
    
        login = Login(Email = email,Password = password)
        login.save()       

    return render(request,"login.html")
   
   
def index(request):
    stock_data = Stock.objects.all()
    data = {
        'stock':stock_data
    }
    return render(request,"index.html",data)


def order(request):
    if request.method == "POST":
        n = request.POST.get('n')
        e = request.POST.get('e')
        o = request.POST.get('o')
        a = request.POST.get('a')
        m = request.POST.get('m')
        Order(Name = n,Email =e,Order = o,Address = a,Query = m).save()
      
    return render(request,"order.html")