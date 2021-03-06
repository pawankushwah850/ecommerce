# Generated by Django 3.1.2 on 2020-10-29 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20201029_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackorder',
            name='delivery',
            field=models.DateField(blank=True, null=True, verbose_name='Enter excepted date'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='orderReceived',
            field=models.BooleanField(blank=True, null=True, verbose_name='Order received'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='orderReceivedDate',
            field=models.DateField(blank=True, null=True, verbose_name='After receiving date'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stage 1'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stage 2'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stage 3'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stage 4'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage5',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stage 5'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage6',
            field=models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='stage 6'),
        ),
        migrations.AlterField(
            model_name='trackorder',
            name='stage7',
            field=models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='stage 7'),
        ),
    ]
