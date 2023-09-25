# Generated by Django 4.2.5 on 2023-09-25 08:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0005_remove_custommenuproduct_custom_menu_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category_image', models.ImageField(default='category_default.png', upload_to='images/DefaultMenu/categories/')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultMenuProductHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('persian_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('max_amount', models.IntegerField(default=2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_image', models.ImageField(default='product_default.png', upload_to='images/DefaultMenu/products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='productHeaders', to='custom_menu.defaultmenucategory')),
            ],
        ),
        migrations.CreateModel(
            name='CustomMenuProductHeaderMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu_header', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='default_menu_maps', to='custom_menu.defaultmenuproductheader')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='default_menu_maps', to='custom_menu.product')),
            ],
        ),
    ]
