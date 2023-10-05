from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from .models import ProductList, Picture


# @admin.register(ProductList)
# class ProductListAdmin(TranslationAdmin):
#     pass


admin.site.register(Picture)
admin.site.register(ProductList)


