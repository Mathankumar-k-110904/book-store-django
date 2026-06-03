from django.db import models

class Order(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book_name}"

