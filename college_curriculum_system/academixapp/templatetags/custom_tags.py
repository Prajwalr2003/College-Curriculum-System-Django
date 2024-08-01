from django import template

register = template.Library()

@register.filter(name='my_range')
def my_range(value):
    return range(1, value + 1)