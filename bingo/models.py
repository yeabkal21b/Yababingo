from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agent_profile")
    operational_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)

    def adjust_credit(self, amount, transaction_type, notes=""):
        # amount: positive for credit, negative for debit
        new_balance = self.operational_credit + amount
        self.operational_credit = new_balance
        self.save()
        Transaction.objects.create(
            agent=self,
            transaction_type=transaction_type,
            amount=amount,
            balance_after_transaction=new_balance,
            notes=notes,
        )

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("ADMIN_CREDIT", "Admin Credit"),
        ("GAME_LAUNCH_COST", "Game Launch Cost"),
        # Add more as needed
    ]
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name="transactions")
    timestamp = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(max_length=24, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-timestamp"]

class GlobalSettings(models.Model):
    min_commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=5.0)
    max_commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=30.0)

class GameSpeed(models.Model):
    name = models.CharField(max_length=32)
    seconds_per_call = models.IntegerField()

class WinningPattern(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

class GameRound(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name="game_rounds")
    created_at = models.DateTimeField(default=timezone.now)
    config_json = models.JSONField()
    board_set = models.JSONField()
    active_board_ids = models.JSONField()
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)