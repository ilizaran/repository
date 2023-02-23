from django import template


register = template.Library()

@register.filter
def filename(value):
    return value.path.split('/')[-1]
