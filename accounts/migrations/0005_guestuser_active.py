# Generated by Django 2.0.7 on 2019-03-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_guestuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestuser',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
