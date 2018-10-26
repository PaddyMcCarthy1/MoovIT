# Generated by Django 2.1.1 on 2018-10-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertys', '0007_auto_20181015_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='county',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='eircode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='postcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='video',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
