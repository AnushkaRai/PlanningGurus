# Generated by Django 2.0.7 on 2019-03-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_booking_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decor', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
