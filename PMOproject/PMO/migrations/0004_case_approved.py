# Generated by Django 2.0.3 on 2018-03-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMO', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='approved',
            field=models.NullBooleanField(),
        ),
    ]