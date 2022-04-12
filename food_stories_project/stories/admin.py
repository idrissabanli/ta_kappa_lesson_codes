from django.contrib import admin
from stories.models import Category, Tag, Recipe


admin.site.register([Category, Tag, Recipe])
