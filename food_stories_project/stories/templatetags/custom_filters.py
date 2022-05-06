from django.template import Library

register = Library()


@register.filter
def truncate(text, count=1):
    sentence = text.split('.')[:int(count)]
    return '.'.join(sentence) + '. ...'