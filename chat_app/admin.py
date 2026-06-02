from django.contrib import admin
from .models import ChatMessage, Customer, Sale

# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(Customer)
admin.site.register(Sale)
