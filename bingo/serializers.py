from rest_framework import serializers
from .models import AgentProfile, Transaction, GameSpeed, WinningPattern, GameRound

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['timestamp', 'transaction_type', 'amount', 'balance_after_transaction', 'notes']

class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['operational_credit', 'commission_percentage']

class GameSpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSpeed
        fields = '__all__'

class WinningPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinningPattern
        fields = '__all__'

class GameRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRound
        fields = '__all__'