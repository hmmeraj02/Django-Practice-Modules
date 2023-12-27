# Generated by Django 5.0 on 2023-12-26 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]