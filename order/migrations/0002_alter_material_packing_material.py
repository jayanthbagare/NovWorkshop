# Generated by Django 4.2.4 on 2023-09-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='packing_material',
            field=models.SmallIntegerField(blank=True, verbose_name='Packing Material Reqd Qty'),
        ),
    ]
