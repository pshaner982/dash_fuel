# Generated by Django 5.1.4 on 2024-12-07 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="tankvolume",
            unique_together={("tank", "timestamp")},
        ),
    ]