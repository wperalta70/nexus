from django.template.defaulttags import register
import random

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def pick_color(list):
    return random.choice(list)