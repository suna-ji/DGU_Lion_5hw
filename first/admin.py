from django.contrib import admin
from .models import Product,Pet,Person,Movie
# Register your models here.

admin.site.register(Product)
admin.site.register(Pet)
admin.site.register(Person)
admin.site.register(Movie)