# Generated by Django 2.1.1 on 2018-10-15 18:56

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('propertys', '0008_auto_20181015_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, default=None, null=True),
        ),
    ]
