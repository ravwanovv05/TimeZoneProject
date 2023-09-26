from django.urls import path

from .views import about, product_details, blog, blog_details, ShoppingCartView, checkout, elements, \
    confirmation, contact, HomeView, ShopView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('about', about),
    path('product_details', product_details),
    path('blog', blog),
    path('blog-details', blog_details),
    path('cart', ShoppingCartView.as_view(), name='cart'),
    path('checkout', checkout),
    path('elements', elements),
    path('confirmation', confirmation),
    path('contact', contact)
]
