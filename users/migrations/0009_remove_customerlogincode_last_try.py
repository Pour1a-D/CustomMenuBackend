# Generated by Django 4.2.5 on 2023-11-20 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customerlogincode_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerlogincode',
            name='last_try',
        ),
    ]