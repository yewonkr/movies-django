# Generated by Django 3.2.21 on 2023-09-16 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20230916_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=200)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actress')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
