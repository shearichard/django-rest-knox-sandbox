# Generated by Django 5.0 on 2024-01-10 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
        migrations.AddField(
            model_name='snippet',
            name='foobar',
            field=models.TextField(blank=True),
        ),
    ]