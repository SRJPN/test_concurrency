# Generated by Django 4.1.7 on 2023-03-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_currentspentsummaryregister"),
    ]

    operations = [
        migrations.AddField(
            model_name="currentspentsummaryregister",
            name="current_spent_summary_id",
            field=models.UUIDField(default="577d63c6-1353-4208-adec-47549986a745"),
            preserve_default=False,
        ),
    ]
