# Generated by Django 3.2.9 on 2021-12-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='mini_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
