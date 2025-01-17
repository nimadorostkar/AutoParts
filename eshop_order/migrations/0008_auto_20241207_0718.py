# Generated by Django 3.2.25 on 2024-12-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0007_auto_20210618_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authority',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ref_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
