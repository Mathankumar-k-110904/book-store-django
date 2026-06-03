from django.shortcuts import render,redirect
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def bookspage(request):
    return render(request,'books.html')

def siginuppage(request):
    if request.method == 'POST':

        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'sigin.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'sigin.html', {
                'error': 'Email already registered'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'sigin.html')

def loginpage(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            user_obj = None

        if user_obj:
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user:
                login(request, user)
                return redirect('order')

        return render(request, 'login.html', {
            'error': 'Invalid Email or Password'
        })

    return render(request, 'login.html')

@login_required
def orderpage(request):
    return render(request, 'order.html', {
        'username': request.user.username
    })
    
    # return render(requset,'order.html')

@login_required
def ordernow(request, book_name, price):

    if request.method == "POST":

        quantity = int(request.POST.get("quantity", 1))
        total_price = price * quantity

        Order.objects.create(
            book_name=book_name,
            book_price=price,
            quantity=quantity,
            total_price=total_price,

            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            pincode=request.POST.get("pincode"),
            payment_method=request.POST.get("payment")
        )

        return render(request, "success.html")

    return render(request, "ordernow.html", {
        "book_name": book_name,
        "book_price": price
    })

def logoutpage(request):
    logout(request)
    return redirect('login')