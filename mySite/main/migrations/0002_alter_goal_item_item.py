# Generated by Django 4.2.3 on 2023-08-20 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal_item',
            name='item',
            field=models.TextField(max_length=200),
        ),
    ]
