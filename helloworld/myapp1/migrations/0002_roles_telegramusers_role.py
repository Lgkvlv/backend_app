# Generated by Django 5.1.7 on 2025-03-21 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lead', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='telegramusers',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp1.roles'),
        ),
    ]
