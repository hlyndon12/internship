# Generated by Django 3.1.7 on 2021-04-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='number',
        ),
        migrations.RemoveField(
            model_name='person',
            name='password',
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]