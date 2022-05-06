from django.template import Library
from stories.models import Category

register = Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()
