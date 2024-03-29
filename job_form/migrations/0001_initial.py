# Generated by Django 5.0.1 on 2024-01-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('occupation', models.CharField(max_length=80)),
            ],
        ),
    ]
