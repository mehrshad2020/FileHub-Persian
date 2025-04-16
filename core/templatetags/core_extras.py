from django import template

register = template.Library()

@register.filter
def split(value, key):
    """
    Returns the split value as a list based on the key.
    Usage: {{ value|split:"/" }}
    """
    return value.split(key) 