# Generated by Django 2.0.7 on 2019-03-20 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emfs', '0021_remove_emf_city'),
        ('events', '0015_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=3, default=1000, max_digits=100, null=True)),
                ('emf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emfs.Emf')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]