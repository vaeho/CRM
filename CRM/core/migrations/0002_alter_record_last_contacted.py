# Generated by Django 5.0.6 on 2024-06-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='last_contacted',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
