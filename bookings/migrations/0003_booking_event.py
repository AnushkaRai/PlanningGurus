# Generated by Django 2.0.7 on 2019-03-14 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_event_image'),
        ('bookings', '0002_auto_20190314_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='event',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]