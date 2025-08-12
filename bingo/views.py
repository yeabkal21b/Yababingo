from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import AgentProfile, Transaction, GameSpeed, WinningPattern, GameRound
from .serializers import (
    TransactionSerializer, AgentProfileSerializer,
    GameSpeedSerializer, WinningPatternSerializer, GameRoundSerializer
)
from django.shortcuts import get_object_or_404

class AgentTransactionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(AgentProfile, user=request.user)
        txs = profile.transactions.all().order_by('-timestamp')
        return Response(TransactionSerializer(txs, many=True).data)

class AgentProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(AgentProfile, user=request.user)
        return Response(AgentProfileSerializer(profile).data)

class GameSpeedList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(GameSpeedSerializer(GameSpeed.objects.all(), many=True).data)

class WinningPatternList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(WinningPatternSerializer(WinningPattern.objects.all(), many=True).data)

class CreateGameRound(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = get_object_or_404(AgentProfile, user=request.user)
        config = request.data.get('config')
        cost = request.data.get('cost')
        if profile.operational_credit < cost:
            return Response({'error': 'Insufficient operational credit'}, status=400)
        # Generate 100 unique bingo boards:
        board_set = generate_unique_boards(100)
        game_round = GameRound.objects.create(
            agent=profile,
            config_json=config,
            board_set=board_set,
            active_board_ids=[str(i) for i in range(100)],
            cost=cost,
        )
        # Deduct credit and create transaction
        profile.adjust_credit(-cost, "GAME_LAUNCH_COST", notes="Game launched")
        return Response(GameRoundSerializer(game_round).data)

def generate_unique_boards(n):
    # Returns a list of n unique bingo boards, using standard bingo card rules
    import random
    def generate_board():
        return {
            'B': random.sample(range(1, 16), 5),
            'I': random.sample(range(16, 31), 5),
            'N': random.sample(range(31, 46), 5),
            'G': random.sample(range(46, 61), 5),
            'O': random.sample(range(61, 76), 5)
        }
    boards = []
    seen = set()
    while len(boards) < n:
        board = generate_board()
        key = tuple(tuple(board[c]) for c in 'BINGO')
        if key not in seen:
            boards.append(board)
            seen.add(key)
    return boards