# Generated by Django 4.2.5 on 2023-10-11 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoice', '0004_invoiceproductdetails_invoiceproducts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='temp_invoices', to='invoice.paymenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='temp_invoices', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempInvoiceProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('count', models.IntegerField(default=1)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='temp_invoice_products', to='invoice.tempinvoice')),
            ],
        ),
        migrations.CreateModel(
            name='TempInvoiceProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('invoice_product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='temp_invoice_product_details', to='invoice.tempinvoiceproducts')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='temp_invoice_product_detail_price', to='custom_menu.price')),
            ],
        ),
    ]
