# Generated by Django 2.0.3 on 2018-03-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField()),
                ('level', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('action', models.TextField()),
                ('cost', models.CharField(max_length=100)),
                ('casualties', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
    ]
