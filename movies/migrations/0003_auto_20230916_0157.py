# Generated by Django 3.2.21 on 2023-09-16 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230915_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actress',
            options={'ordering': ['enName']},
        ),
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['title']},
        ),
    ]
