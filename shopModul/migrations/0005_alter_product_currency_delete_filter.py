# Generated by Django 4.2 on 2023-09-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopModul', '0004_remove_propertyvalue_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, choices=[('₽', '₽'), ('$', '$')], max_length=1, null=True),
        ),
        migrations.DeleteModel(
            name='Filter',
        ),
    ]