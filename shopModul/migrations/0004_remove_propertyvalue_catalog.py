# Generated by Django 4.2 on 2023-08-31 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopModul', '0003_remove_property_value_propertyvalue_catalog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyvalue',
            name='catalog',
        ),
    ]