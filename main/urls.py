from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import about, product_details, blog, blog_details, ShoppingCartView, checkout, elements, \
    confirmation, contact, HomeView, ShopView, IncrementCountView, DecrementCountView

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
    path('contact', contact),
    path('increment-count', csrf_exempt(IncrementCountView.as_view()), name='increment'),
    path('decrement-count', csrf_exempt(DecrementCountView.as_view()), name='decrement')
]
