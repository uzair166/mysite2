# Generated by Django 3.1.5 on 2021-01-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]