from django.contrib import admin
from .models import User, AgentProfile, Transaction, GlobalSettings, GameSpeed, WinningPattern, GameRound

class TransactionInline(admin.TabularInline):
    model = Transaction
    readonly_fields = ('timestamp', 'transaction_type', 'amount', 'balance_after_transaction', 'notes')
    can_delete = False
    extra = 0

@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'operational_credit', 'commission_percentage')
    readonly_fields = ('user',)
    inlines = [TransactionInline]
    actions = None

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = AgentProfile.objects.get(pk=obj.pk)
            if old_obj.operational_credit != obj.operational_credit:
                amount = obj.operational_credit - old_obj.operational_credit
                obj.adjust_credit(amount, "ADMIN_CREDIT", notes="Manual admin adjustment")
        super().save_model(request, obj, form, change)

admin.site.register(User)
admin.site.register(GlobalSettings)
admin.site.register(GameSpeed)
admin.site.register(WinningPattern)
admin.site.register(GameRound)