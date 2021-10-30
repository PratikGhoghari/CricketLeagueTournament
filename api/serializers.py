from django.db.models import fields
from rest_framework import serializers
from api.models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team_id.name')
    opponent_name = serializers.CharField(source='opponent_id.name')
    toss_winner = serializers.CharField(source='toss_win_id.name')
    toss_loser = serializers.CharField(source='toss_lose_id.name')
    match_winner = serializers.CharField(source='match_win_id.name')
    match_losser = serializers.CharField(source='match_lose_id.name')
    man_of_the_match = serializers.CharField(source='man_of_match.player_name')
    bowler_of_the_match = serializers.CharField(source='bowler_of_match.player_name')
    class Meta:
        model = Match
        fields = ['team_name', 'opponent_name', 'toss_winner', 'toss_loser', 'match_winner', 'match_losser', 'man_of_the_match', 'bowler_of_the_match']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'