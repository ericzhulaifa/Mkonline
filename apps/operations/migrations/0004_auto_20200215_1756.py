# Generated by Django 2.2.9 on 2020-02-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=0, verbose_name='播放顺序'),
        ),
    ]
