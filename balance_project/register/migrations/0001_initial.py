# Generated by Django 4.2.13 on 2024-06-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('repeat_password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registers',
                'ordering': ['name'],
            },
        ),
    ]
