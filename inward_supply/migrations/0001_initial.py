# Generated by Django 5.1.6 on 2025-03-12 11:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bill_number', models.CharField(max_length=255)),
                ('retailer_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inward_supply.invoicebill')),
            ],
        ),
    ]
