# Generated by Django 3.2.21 on 2023-09-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20230921_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actress',
            name='rank',
        ),
        migrations.AddField(
            model_name='actress',
            name='debut',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='actress',
            name='info',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='info',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
