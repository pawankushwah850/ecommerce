# Generated by Django 3.1.2 on 2020-10-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_trackorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackorder',
            name='stage6',
            field=models.CharField(default='-', max_length=200, verbose_name='stage 6'),
        ),
        migrations.AddField(
            model_name='trackorder',
            name='stage7',
            field=models.CharField(default='-', max_length=200, verbose_name='stage 7'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage4',
            field=models.CharField(max_length=200, verbose_name='stage 4'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage5',
            field=models.CharField(max_length=200, verbose_name='stage 5'),
        ),
    ]