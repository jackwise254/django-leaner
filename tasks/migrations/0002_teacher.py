# Generated by Django 4.0.6 on 2022-08-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=64, verbose_name='First name')),
                ('lname', models.CharField(max_length=64, verbose_name='Last name')),
                ('email', models.CharField(max_length=64, verbose_name='email name')),
                ('class_id', models.CharField(max_length=64, verbose_name='class name')),
            ],
        ),
    ]
