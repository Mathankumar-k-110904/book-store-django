from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('books/', views.bookspage, name='books'),
    path('sigin/', views.siginuppage, name='signin'),
    path('order/', views.orderpage, name='order'),
    path('login/',views.loginpage,name='login'),
    path('ordernow/<str:book_name>/<int:price>/', views.ordernow, name='ordernow'),
]
