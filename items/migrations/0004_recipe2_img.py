# Generated by Django 5.0.6 on 2024-07-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_delete_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe2',
            name='img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='img_store/'),
        ),
    ]
