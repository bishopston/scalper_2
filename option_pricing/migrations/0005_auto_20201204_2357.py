# Generated by Django 3.1.3 on 2020-12-04 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option_pricing', '0004_auto_20201202_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionsymbol',
            name='strike',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
