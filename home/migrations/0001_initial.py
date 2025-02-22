# Generated by Django 5.1.3 on 2024-11-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=20)),
                ('phone', models.IntegerField(max_length=10)),
                ('category', models.CharField(choices=[('Orthopedics', 'Orthopedics'), ('General Medicine', 'General Medicine'), ('Ophthalmologist', 'Ophthalmologist'), ('Skin Care', 'Skin Care')], default='General Medicine', max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField(blank=True, null=True)),
                ('sent', models.TextField(max_length=30)),
            ],
        ),
    ]
