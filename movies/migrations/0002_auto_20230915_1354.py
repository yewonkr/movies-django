# Generated by Django 3.2.21 on 2023-09-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actress',
            name='birth',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='actress',
            name='height',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='actress',
            name='rank',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
