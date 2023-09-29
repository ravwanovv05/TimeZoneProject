from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductList(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pics')
    price = models.FloatField()
    description = models.TextField()



class ShoppingCart(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    uploaded_date = models.DateTimeField(auto_now_add=True)




