from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/categories/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', 'title')
    
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    title = models.CharField('Title', max_length=50, db_index=True)
    short_description = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='media/recipes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)