from django.contrib import admin
from stories.models import Category, Tag, Recipe


admin.site.register([Tag])


class RecipeInlineAdmin(admin.TabularInline):
    model = Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (RecipeInlineAdmin, )

    


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category__title', 'author__username')
    list_filter = ('category', 'author__username')
    list_display = ('title', 'author', 'category', 'created_at')
    fieldsets = (
        ('Informations', {
            'fields': ('title', 'slug', 'content', 'image', 'short_description', )
        }),
        ('Relations', {
            'fields': ('tags', ('category', 'author', )),
            'classes': ('collapse',)
        })
        )



