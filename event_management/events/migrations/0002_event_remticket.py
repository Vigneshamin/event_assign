# Generated by Django 3.2.9 on 2022-02-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='remticket',
            field=models.IntegerField(null=True),
        ),
    ]