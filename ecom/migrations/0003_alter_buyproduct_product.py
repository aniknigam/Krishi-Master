# Generated by Django 4.2.2 on 2023-06-30 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_buyproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproduct',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='productbuyer', to='ecom.productlisting'),
        ),
    ]
