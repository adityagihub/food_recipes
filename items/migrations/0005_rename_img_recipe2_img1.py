# Generated by Django 5.0.6 on 2024-07-05 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_recipe2_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe2',
            old_name='img',
            new_name='img1',
        ),
    ]
