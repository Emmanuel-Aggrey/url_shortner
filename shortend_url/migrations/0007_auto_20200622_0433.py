# Generated by Django 2.2.10 on 2020-06-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortend_url', '0006_auto_20200622_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='hash_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='link',
            name='hash_url',
            field=models.URLField(blank=True),
        ),
    ]