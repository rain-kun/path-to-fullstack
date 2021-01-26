# Generated by Django 3.0.8 on 2020-09-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_list_bid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['types']},
        ),
        migrations.RemoveField(
            model_name='list',
            name='bid',
        ),
        migrations.AddField(
            model_name='bid',
            name='title',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='types',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
    ]