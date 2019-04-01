# Generated by Django 2.0.7 on 2019-03-12 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emfs', '0007_auto_20190312_1013'),
        ('events', '0006_event_emf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='emf',
        ),
        migrations.AddField(
            model_name='event',
            name='emf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='emfs.Emf'),
        ),
    ]