from django import template
register = template.Library()


@register.simple_tag
def get_key(obj, val1, val2):
    return obj['%s%s' % (val1, val2)]
