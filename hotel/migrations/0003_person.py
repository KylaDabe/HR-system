# Generated by Django 4.0.5 on 2022-06-20 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]