# Generated by Django 4.2.5 on 2023-11-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customeruser_details_customerloginsession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
