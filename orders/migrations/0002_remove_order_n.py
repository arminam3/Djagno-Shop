# Generated by Django 4.1 on 2022-09-30 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='n',
        ),
    ]
