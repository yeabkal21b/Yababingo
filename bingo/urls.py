from django.urls import path
from .views import (
    AgentProfileView, AgentTransactionList,
    GameSpeedList, WinningPatternList, CreateGameRound
)

urlpatterns = [
    path('api/profile/', AgentProfileView.as_view()),
    path('api/transactions/', AgentTransactionList.as_view()),
    path('api/game-speeds/', GameSpeedList.as_view()),
    path('api/winning-patterns/', WinningPatternList.as_view()),
    path('api/create-game/', CreateGameRound.as_view()),
]