# Generated by Django 4.2.7 on 2023-11-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0003_alter_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('customer', 'customer'), ('mechanic', 'mechanic')], default='customer', max_length=10),
        ),
    ]
