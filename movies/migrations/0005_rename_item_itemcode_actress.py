# Generated by Django 3.2.21 on 2023-09-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_itemcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcode',
            old_name='item',
            new_name='actress',
        ),
    ]