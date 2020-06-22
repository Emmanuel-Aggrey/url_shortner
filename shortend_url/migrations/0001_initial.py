# Generated by Django 2.2.10 on 2020-06-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(blank=True, max_length=10)),
                ('url', models.URLField()),
                ('hash_url', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
