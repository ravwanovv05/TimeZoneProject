from django import template


register = template.Library()


@register.simple_tag
def total_price(price, count):
    total = int(price) * int(count)
    if total > 0:
        return total

