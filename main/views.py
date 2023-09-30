import json
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main.models import ProductList, ShoppingCart
from main.utils import increment_count, decrement_count


class HomeView(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        products = ProductList.objects.all()[2:]
        self.context.update({'products': products})
        return render(request, self.template_name, self.context)


class ShopView(View):
    template_name = "shop.html"
    context = {}

    def get(self, request):
        try:
            products = ProductList.objects.all()[:2]
            self.context.update({'products': products})
            return render(request, self.template_name, self.context)
        except:
            return redirect('/')

    def post(self, request):
        try:
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
        except:
            messages.error(request, "Please, enter your account!")
        return redirect('shop')


class ShoppingCartView(View):
    template_name = "cart.html"
    context = {}

    def get(self, request):
        try:
            shopping_cart = ShoppingCart.objects.filter(user=request.user).values('product_id')
            products = ProductList.objects.filter(pk__in=shopping_cart)
            data = []
            for product in products:
                shop = ShoppingCart.objects.get(Q(user=request.user) & Q(product=product))
                product.count = shop.count
                data.append(product)
            self.context.update({'products': data})
            return render(request, self.template_name, self.context)
        except:
            messages.error(request, 'Enter your account!')
            return redirect('/')

    def post(self, request):
        try:
            id = request.POST.get('id')
            user = request.user
            shopping_cart = ShoppingCart.objects.get(Q(product_id=id), Q(user=user))
            shopping_cart.delete()
            return redirect('/cart')
        except:
            return redirect('/cart')


class IncrementCountView(View):
    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = increment_count(id, request.user)
        return JsonResponse({'result': result})


class DecrementCountView(View):
    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = decrement_count(id, request.user)
        return JsonResponse({'result': result})


class AddProductView(CreateView):
    model = ProductList
    template_name = "add_product.html"
    fields = ('name', 'price', 'description')

    def post(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        author = request.user

        product = ProductList.objects.create(
            name=name,
            price=price,
            description=description,
            author=author
        )
        product.save()
        return redirect('/add-product')



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
