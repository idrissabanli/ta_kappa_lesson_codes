from modeltranslation.translator import translator, TranslationOptions
from stories.models import Recipe, Category, Tag


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


class TagTranslationOptions(TranslationOptions):
    fields = ('title', )


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'content',)


translator.register(Recipe, RecipeTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Category, CategoryTranslationOptions)