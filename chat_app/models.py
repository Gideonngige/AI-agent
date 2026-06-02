from django.db import models

class ChatMessage(models.Model):
    role = models.CharField(max_length=20)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.amount}"