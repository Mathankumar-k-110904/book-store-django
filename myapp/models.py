from django.db import models

# Create your models here.

class signin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    # confrim_password = models.CharField(max_length=128)


from django.db import models

class Order(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()

    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()

    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    payment_method = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book_name}"