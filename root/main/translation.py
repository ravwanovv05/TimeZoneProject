from modeltranslation.translator import TranslationOptions, translator

from main.models import ProductList


class ProductListTranslation(TranslationOptions):
    fields = ('name', 'description')


translator.register(ProductList, ProductListTranslation)