# Generated by Django 4.2.5 on 2023-10-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_alter_invoice_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempinvoiceproductdetails',
            name='invoice_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp_invoice_product_details', to='invoice.tempinvoiceproducts'),
        ),
        migrations.AlterField(
            model_name='tempinvoiceproducts',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp_invoice_products', to='invoice.tempinvoice'),
        ),
    ]
