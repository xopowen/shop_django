# Generated by Django 4.1.2 on 2023-08-30 15:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='catalog/')),
                ('order', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])])),
            ],
        ),
        migrations.CreateModel(
            name='ImgLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('link', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='manufacturer/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='news/%Y/%m/%d/')),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'A news',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('show_popup', models.BooleanField(default=False)),
                ('show_filter', models.BooleanField(default=False)),
                ('selected', models.BooleanField()),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Proportion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('prefix', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='VideoLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='shopModul/static/shop/move/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav', 'mp4', 'webm'])])),
            ],
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=255, unique=True)),
                ('show_menu', models.BooleanField(default=False)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopModul.property')),
            ],
            options={
                'verbose_name': 'Value of Propert',
                'verbose_name_plural': 'Values of Property',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('act', models.IntegerField(blank=True, null=True)),
                ('amt', models.IntegerField(default=0)),
                ('price', models.FloatField(blank=True, null=True)),
                ('old_price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('₽', '₽'), ('$', '$')], max_length=1)),
                ('technical_feature', models.TextField(blank=True, null=True)),
                ('article', models.CharField(default='000 000', max_length=12)),
                ('YTP', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('visibility', models.BooleanField(default=False)),
                ('catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopModul.catalog')),
                ('documents', models.ManyToManyField(blank=True, null=True, to='shopModul.document')),
                ('img', models.ManyToManyField(blank=True, null=True, to='shopModul.imglink')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopModul.manufacturer')),
                ('proportion', models.ManyToManyField(blank=True, null=True, to='shopModul.proportion')),
                ('video', models.ManyToManyField(blank=True, null=True, to='shopModul.videolink')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='paragraph/')),
                ('text', models.TextField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopModul.news')),
            ],
            options={
                'verbose_name': 'Paragraph',
                'verbose_name_plural': 'Paragraphs',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopModul.catalog')),
            ],
            options={
                'verbose_name': 'Filter',
                'verbose_name_plural': 'Filters',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('comment', models.TextField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('head', models.CharField(max_length=255)),
                ('subtitle', models.TextField(blank=True)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopModul.catalog')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopModul.manufacturer')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
    ]
