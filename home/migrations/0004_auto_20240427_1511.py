# Generated by Django 3.2.24 on 2024-04-27 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reviewrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='reviewrating',
            name='product',
        ),
    ]
