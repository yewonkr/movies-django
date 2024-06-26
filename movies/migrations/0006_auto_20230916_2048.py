# Generated by Django 3.2.21 on 2023-09-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_item_itemcode_actress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.RemoveField(
            model_name='movies',
            name='actress',
        ),
        migrations.AddField(
            model_name='actress',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movies.Movies'),
        ),
    ]
