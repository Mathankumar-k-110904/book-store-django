from django.shortcuts import render,redirect
from .models import signin,Order

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def bookspage(request):
    return render(request,'books.html')

def siginuppage(request):
    if request.method== 'POST':
        Name = request.POST.get('name')
        Age = request.POST.get("dob")
        Mail = request.POST.get("email")
        Password = request.POST.get("password")
        confirm_password = request.POST.get('confirm_password')

        if Password != confirm_password:
            return render(request, 'sigin.html', {'error': 'Passwords do not match'})
        
        if signin.objects.filter(email=Mail).exists():
            return render(request, 'sigin.html', {
                'error': 'Email already registered'
            })
        
        signin.objects.create(username=Name,date_of_birth=Age,email=Mail,password=Password)
        
        return redirect('login')

    return render(request,'sigin.html')

def loginpage(request):
    if request.method == 'POST':
        u_name = request.POST.get('name')
        u_mail = request.POST.get('email')
        u_password = request.POST.get('password')

        user = signin.objects.filter(
            username = u_name,
            email = u_mail,
            password = u_password,
        ).first()

        if user:
            request.session['username']= user.username
            request.session['email']= user.email
            request.session['password']= user.password
            return redirect('order')
        
        else:
            return render(request,'login.html',{'error':'invalid input'})
    return render(request,'login.html')

def orderpage(requset):
    if 'username' in requset.session:
        username = requset.session['username']
        return render(requset,'order.html',{'username':username})
    return redirect('login')
    
    # return render(requset,'order.html')


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

