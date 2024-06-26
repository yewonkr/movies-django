# Generated by Django 3.2.21 on 2023-09-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20230916_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actress',
            name='movies',
        ),
        migrations.AddField(
            model_name='movies',
            name='actress',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movies.Actress'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
