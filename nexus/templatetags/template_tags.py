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

@register.filter
def filter(object, attribute, value):
    return object.filter(attribute = value)

# This filter receives a ticket's priority, and returns a color based on the priority
@register.filter
def get_priority_color(priority):
    if priority == 'ALTA':
        return 'danger'
    
    if priority == 'MEDIA':
        return 'warning'

    if priority == 'BAJA':
        return 'primary'

    return 'secondary'