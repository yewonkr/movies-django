# Generated by Django 3.2.21 on 2023-10-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20230925_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actress',
            name='enName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='actress',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
