# Generated by Django 3.2.5 on 2021-08-23 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, unique=True)),
                ('details', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Temporary_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_key', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(max_length=1000, null=True)),
                ('title', models.CharField(max_length=1000, null=True)),
                ('ISBN', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=350, null=True)),
                ('published_city', models.CharField(max_length=300, null=True)),
                ('published_year', models.CharField(max_length=4, null=True)),
                ('details', models.TextField(max_length=1000, null=True)),
                ('search_number', models.IntegerField(unique=True)),
                ('is_complete_search', models.BooleanField(default=False)),
                ('price', models.FloatField(blank=True, null=True)),
                ('bought_date', models.DateField(blank=True, null=True)),
                ('categories', models.TextField(max_length=1000)),
                ('physical_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='books_online.shelve')),
            ],
        ),
        migrations.CreateModel(
            name='Book_to_accept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_key', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(max_length=1000, null=True)),
                ('title', models.CharField(max_length=1000, null=True)),
                ('ISBN', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=350, null=True)),
                ('published_city', models.CharField(max_length=300, null=True)),
                ('published_year', models.CharField(max_length=4, null=True)),
                ('details', models.TextField(max_length=1000, null=True)),
                ('search_number', models.IntegerField(unique=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('bought_date', models.DateField(blank=True, null=True)),
                ('categories', models.TextField(max_length=1000)),
                ('physical_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='books_online.shelve')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_key', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('ISBN', models.CharField(max_length=13)),
                ('publisher', models.CharField(blank=True, max_length=350, null=True)),
                ('published_city', models.CharField(blank=True, max_length=300, null=True)),
                ('published_year', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('bought_date', models.DateField(blank=True, null=True)),
                ('details', models.TextField(blank=True, max_length=1000, null=True)),
                ('categories', models.TextField(blank=True, max_length=1000, null=True)),
                ('categories_fk', models.ManyToManyField(blank=True, to='books_online.BookCategory')),
                ('physical_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books_online.shelve')),
            ],
        ),
    ]
