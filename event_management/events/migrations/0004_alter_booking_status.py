# Generated by Django 3.2.9 on 2022-02-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_booking_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')], default='Booked', max_length=100, null=True),
        ),
    ]
