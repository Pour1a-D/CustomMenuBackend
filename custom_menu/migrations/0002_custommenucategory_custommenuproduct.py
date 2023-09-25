# Generated by Django 4.2.5 on 2023-09-25 06:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category_image', models.ImageField(default='category_default.png', upload_to='images/categories/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomMenuProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('persian_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('max_amount', models.IntegerField(default=2)),
                ('is_active', models.BooleanField(default=True)),
                ('has_tax', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_image', models.ImageField(default='product_default.png', upload_to='images/products/')),
                ('custom_menu_category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='custom_menu.custommenucategory')),
                ('used_products', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='used_products', to='custom_menu.product')),
            ],
        ),
    ]
