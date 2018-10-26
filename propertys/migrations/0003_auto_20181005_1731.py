# Generated by Django 2.1.1 on 2018-10-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertys', '0002_auto_20181005_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='property',
            name='floorplan',
            field=models.ImageField(blank=True, default=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='property',
            name='mapping',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='publish_date',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
