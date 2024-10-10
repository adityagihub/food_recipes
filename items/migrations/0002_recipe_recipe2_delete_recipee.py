# Generated by Django 5.0.6 on 2024-07-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_description', models.CharField(max_length=100)),
                ('recipe_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='recipe2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=100)),
                ('rdes', models.CharField(max_length=100)),
                ('rprice', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='recipee',
        ),
    ]
