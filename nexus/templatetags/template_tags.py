from django.template.defaulttags import register
import random

# This is used to generate the breadcrumb HTML for every template
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# This filter picks a random color from a colors list
# This is used to pick a background color for a project's symbol
@register.filter
def pick_color(list):
    return random.choice(list)

# This filter returns true if the user belongs to a certain group
@register.filter
def has_role(user, role):
    return user.groups.filter(name = role).exists()