# Generated by Django 5.0.4 on 2024-05-01 02:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_remove_article_authors_en_remove_article_authors_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='author_description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='author_description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='author_description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
