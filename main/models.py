from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductList(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def create(self, validated_data):
        print(validated_data)
        return super().save(**validated_data)


class Picture(models.Model):
    image = models.ImageField(upload_to='pics')
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], default=1
    )
    uploaded_date = models.DateTimeField(auto_now_add=True)




