# Generated by Django 3.2.21 on 2023-09-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20230923_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actress',
            name='info',
            field=models.TextField(default='NO DATA', null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='info',
            field=models.TextField(default='NO DATA', null=True),
        ),
    ]
