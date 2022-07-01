from datetime import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stories.models import Recipe
from slugify import slugify

@receiver(post_save, sender=Recipe)
def slug_generator_recipe_model(sender, instance, created, **kwargs):
        replacements = [['Ə', 'e']]
        slug = slugify(instance.title, replacements=replacements) + '-' + str(instance.id)
        if not slug == instance.slug:
            instance.slug = slug
            instance.save()


# @receiver(pre_save, sender=Recipe)
# def slug_generator_recipe_model(sender, instance, **kwargs):
#     if not instance.slug:
#         replacements = [['Ə', 'e']]
#         slug = slugify(instance.title, replacements=replacements) + datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
#         instance.slug = slug