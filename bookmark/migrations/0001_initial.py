# Generated by Django 3.1.2 on 2020-10-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('url', models.URLField(verbose_name='Site URL')),
            ],
        ),
    ]
