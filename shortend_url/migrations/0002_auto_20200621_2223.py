# Generated by Django 2.2.10 on 2020-06-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortend_url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='hash_url',
            field=models.URLField(),
        ),
    ]
