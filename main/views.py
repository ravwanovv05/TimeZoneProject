from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from main.models import ProductList, ShoppingCart
from main.utils import increment_count, decrement_count


class HomeView(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name)


class ShopView(View):
    template_name = "shop.html"
    context = {}

    def get(self, request):
        products = ProductList.objects.all()
        self.context.update({'products': products})
        return render(request, self.template_name, self.context)

    def post(self, request):
        id = request.POST.get('id')
        user_id = request.user.id
        products_id = set([i['product_id'] for i in ShoppingCart.objects.filter(user_id=user_id).values('product_id')])
        if int(id) not in list(products_id):
            shopping_cart = ShoppingCart.objects.create(
                product_id=id,
                user_id=user_id
            )
            shopping_cart.save()
            messages.info(request, 'Successfully added!')
        return redirect('shop')


class ShoppingCartView(View):
    template_name = "cart.html"
    context = {}

    def get(self, request):
        shopping_cart = ShoppingCart.objects.filter(user=request.user).values('product_id')
        products = ProductList.objects.filter(pk__in=shopping_cart)
        self.context.update({'products': products})
        return render(request, self.template_name, self.context)

    def post(self, request):
        id = request.POST.get('id')
        user = request.user
        shopping_cart = ShoppingCart.objects.get(Q(product_id=id), Q(user=user))
        shopping_cart.delete()
        return redirect('/cart')


class IncrementCountView(View):
    def post(self, request):
        id = request.POST.get('id')
        result = increment_count(id)
        return JsonResponse({'result': result})


class DecrementCountView(View):
    def post(self, request):
        id = request.POST.get('id')
        result = decrement_count(id)
        return JsonResponse({'result': result})


def about(request):
    return render(request, "about.html")


def product_details(request):
    return render(request, "product_details.html")


def blog(request):
    return render(request, "blog.html")


def blog_details(request):
    return render(request, "blog-details.html")


def checkout(request):
    return render(request, "checkout.html")


def elements(request):
    return render(request, "elements.html")


def confirmation(request):
    return render(request, "confirmation.html")


def contact(request):
    return render(request, "contact.html")
