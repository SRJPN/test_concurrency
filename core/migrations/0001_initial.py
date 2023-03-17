# Generated by Django 4.1.7 on 2023-03-17 11:15

from decimal import Decimal
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CurrentSpentSummary",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "cleared_balance",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0"),
                        editable=False,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "reward_balance",
                    models.DecimalField(
                        decimal_places=6,
                        default=Decimal("0"),
                        editable=False,
                        max_digits=20,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "current_spent_summary",
            },
        ),
    ]