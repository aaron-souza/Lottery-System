# Generated by Django 2.2.2 on 2019-06-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]