# Generated by Django 5.1.4 on 2025-01-08 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_slider', '0003_bannerleft_bannerright'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BannerLeft',
        ),
        migrations.DeleteModel(
            name='BannerRight',
        ),
    ]