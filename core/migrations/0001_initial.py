# Generated by Django 3.2.7 on 2022-07-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ITA_Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ita', models.CharField(max_length=100)),
                ('eng', models.CharField(max_length=100)),
            ],
        ),
    ]
