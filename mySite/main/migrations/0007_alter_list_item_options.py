# Generated by Django 4.2.3 on 2023-08-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_list_item_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list_item',
            options={'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
    ]
