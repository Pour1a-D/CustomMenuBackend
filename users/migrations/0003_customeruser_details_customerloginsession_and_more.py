# Generated by Django 4.2.5 on 2023-11-20 14:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customeruser_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='details',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='CustomerLoginSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('last_try', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_ip', models.CharField(max_length=255)),
                ('client_user_agent', models.CharField(max_length=255)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLoginCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField()),
                ('failed_tries', models.PositiveIntegerField()),
                ('last_try', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_ip', models.CharField(max_length=255)),
                ('client_user_agent', models.CharField(max_length=255)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customeruser')),
            ],
        ),
    ]
