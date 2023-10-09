# Generated by Django 4.2.5 on 2023-10-09 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='invoice_details', to='invoice.invoice')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='invoice_detail_price', to='custom_menu.price')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='invoices', to='invoice.paymenttype'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='invoices', to=settings.AUTH_USER_MODEL),
        ),
    ]
