# Generated by Django 2.2.10 on 2020-06-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortend_url', '0010_auto_20200623_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shortened_url',
            field=models.URLField(blank=True),
        ),
    ]
