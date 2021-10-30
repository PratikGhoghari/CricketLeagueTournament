from django.db.models import manager
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import *
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def home(request):
    context = {
        'api/allteams/': 'Get all the teams of tournament',
        'api/countries/' : 'Get all the countries participated in tournament',
        'api/playerprofile/<id>/' : 'Get player profile of a player by passing player id',
        'api/playerprofiles/' : 'Get all the profile of players',
        'api/listofmatches/' : 'Get list of all the matches happened in the tournament',
        'api/matchsummary/<id>/' : 'Get match summary of an individual match such as won_by, lost_by etc',
        'api/matchsummaries/' : 'Get all match summaries happened in the tournament',
        'api/venues' : 'Get the venue (Stadium name) of all the matches happened in the tournament'
    }
    return Response(context)

@api_view(['GET'])
def get_all_teams(request):
    teams = Team.objects.all()
    teams_serializer = TeamSerializer(teams, many=True)
    return Response(teams_serializer.data)

@api_view(['GET'])
def get_countries(request):
    countries = Country.objects.all()
    countries_serializer = CountrySerializer(countries, many=True)
    return Response(countries_serializer.data)

@api_view(["GET"])
def get_player_profile(request, pk):
    player = Player.objects.get(id=pk)
    player_serializer = PlayerSerializer(player)
    return Response(player_serializer.data)

@api_view(["GET"])
def get_player_profiles(request):
    players= Player.objects.all()
    player_serializer = PlayerSerializer(players, many=True)
    return Response(player_serializer.data)

@api_view(['GET'])
def get_all_matches(request):                             
    matches =  Match.objects.all()
    match_serializer = MatchSerializer(matches, many=True)
    return Response(match_serializer.data)

@api_view(['GET'])
def get_match_summary(request, pk):
    match_summaries = Match.objects.filter(id=pk)
    #print(match_summaries)
    #print(match_summaries.bowler_of_match)
    match_serializer = MatchSerializer(match_summaries,many=True)
    #return render(request, 'api/match_summary.html', context=context)
    return Response(match_serializer.data)

@api_view(['GET'])
def get_all_match_summary(request):
    match_summaries = Match.objects.all()
    match_serializer = MatchSerializer(match_summaries, many=True)
    '''
    context = {
        "match_summaries":match_summaries
    }
    '''
    #return render(request, 'api/match_summary.html', context=context)  
    return Response(match_serializer.data)

@api_view(['GET'])
def get_venues(request):
    match_venues = Match.objects.values_list('Venue', flat=True)
    match_venues = set(match_venues)
    return Response(match_venues)
