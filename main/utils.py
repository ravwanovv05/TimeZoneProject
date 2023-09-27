from main.models import ShoppingCart


def increment_count(id):
    try:
        shopping_cart = ShoppingCart.objects.get(pk=id)
        shopping_cart += 1
        shopping_cart.save()
    except:
        return False
    return True


def decrement_count(id):
    try:
        shopping_cart = ShoppingCart.objects.get(pk=id)
        shopping_cart -= 1
        shopping_cart.save()
    except:
        return False
    return True