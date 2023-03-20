from decimal import Decimal
from uuid import uuid4
from django.db import models, transaction
from core.exceptions import (
    InvalidCurrentSpentSummary,
)
from django.db.models import F

# Create your models here.


class CurrentSpentSummaryManager(models.Manager):
    # @transaction.atomic()
    def update_current_spent_summary(
        self,
        existing_spent_summary_id,
        reward_balance: Decimal = None,
        cleared_balance: Decimal = None,
    ):
        # with transaction.atomic():
        # to_update = self.model.objects.get(pk=existing_spent_summary_id)
        # to_update.cleared_balance = Decimal(to_update.cleared_balance) + Decimal(cleared_balance)
        # to_update.reward_balance = Decimal(to_update.reward_balance) + Decimal(reward_balance)
        # to_update.save()
        # to_update.refresh_from_db()
        # return to_update

        to_update = self.model.objects.filter(pk=existing_spent_summary_id)
        is_updated = to_update.update(
            cleared_balance=F("cleared_balance") + cleared_balance,
            reward_balance=F("reward_balance") + reward_balance,
        )
        if not is_updated:
            raise InvalidCurrentSpentSummary

        return to_update.first()


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

class CurrentSpentSummaryRegisterManager(models.Manager):
    pass

class CurrentSpentSummaryRegister(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    current_spent_summary_id = models.UUIDField(null=False)
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
    objects = CurrentSpentSummaryRegisterManager()

    class Meta:
        db_table = "current_spent_summary_history"
