# Generated by Django 4.2.3 on 2023-08-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_goal_item_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Goal_item',
        ),
    ]