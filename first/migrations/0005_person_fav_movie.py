# Generated by Django 2.0.13 on 2019-04-09 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fav_movie',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
