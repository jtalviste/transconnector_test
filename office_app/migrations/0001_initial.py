# Generated by Django 5.0 on 2023-12-23 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_checked', models.DateTimeField()),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_app.office')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_app.person')),
            ],
        ),
    ]