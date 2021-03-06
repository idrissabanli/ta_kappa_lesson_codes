# Generated by Django 4.0.3 on 2022-07-05 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='short_description_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='short_description_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='short_description_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug_az',
            field=models.SlugField(max_length=80, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug_en',
            field=models.SlugField(max_length=80, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug_ru',
            field=models.SlugField(max_length=80, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_az',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_en',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_ru',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_ru',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
