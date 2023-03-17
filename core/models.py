from decimal import Decimal
from uuid import uuid4
from django.db import models
from core.exceptions import (
    InvalidCurrentSpentSummary,
)

# Create your models here.


class CurrentSpentSummaryManager(models.Manager):
    def update_current_spent_summary(
        self,
        existing_spent_summary_id,
        reward_balance: Decimal = None,
        cleared_balance: Decimal = None,
    ):
        is_updated = self.model.objects.filter(id=existing_spent_summary_id,).update(
            cleared_balance=F("cleared_balance") + cleared_balance,
            reward_balance=F("reward_balance") + reward_balance,
        )

        if not is_updated:
            raise InvalidCurrentSpentSummary
        return self.model.objects.get(pk=existing_spent_summary_id)


class CurrentSpentSummary(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    cleared_balance = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        editable=False,
        default=Decimal(0.00),
        null=True,
    )
    reward_balance = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        editable=False,
        default=Decimal(0.00),
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CurrentSpentSummaryManager()

    class Meta:
        db_table = "current_spent_summary"
