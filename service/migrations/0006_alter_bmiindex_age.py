# Generated by Django 5.1.3 on 2024-11-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_bmiindex_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmiindex',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
