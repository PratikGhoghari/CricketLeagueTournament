from django.db.models import manager
from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import *
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core import serializers
import json
def home(request):
    return HttpResponse("<h1>Cricket League Tournament</h1>")

@api_view(['GET'])
def get_all_teams(request):
    teams = Team.objects.all()
    context = {
        "all_teams":teams
    }
    return render(request, 'api/all_teams.html', context=context)

@api_view(['GET'])
def get_countries(request):
    countries = Country.objects.all()
    context = {
        "countries":countries
    }
    return render(request, 'api/countries.html', context=context)

@api_view(["GET"])
def get_player_profile(request, pk):
    player = Player.objects.get(id=pk)
    context = {
        "player":player
    }
    return render(request, 'api/player_profile.html', context=context)

@api_view(["GET"])
def get_player_profiles(request):
    players= Player.objects.all()
    context = {
        "players":players
    } 
    return render(request, 'api/player_profiles.html', context=context)

@api_view(['GET'])
def get_all_matches(request):                             
    matches =  Match.objects.all()
    context = {
        "matches":matches
    } 
    return render(request, 'api/list_of_matches.html', context=context)

@api_view(['GET'])
def get_match_summary(request, pk):
    match_summaries = Match.objects.filter(id=pk)
    #print(match_summaries)
    #print(match_summaries.bowler_of_match)
    #match_serializer = MatchSerializer(match_summaries)
    context = {
        "match_summaries":match_summaries
    }
    return render(request, 'api/match_summary.html', context=context)


@api_view(['GET'])
def get_all_match_summary(request):
    match_summaries = Match.objects.all()
    context = {
        "match_summaries":match_summaries
    }
    return render(request, 'api/match_summary.html', context=context)  


@api_view(['GET'])
def get_venues(request):
    match_venues = Match.objects.values_list('Venue', flat=True)
    match_venues = set(match_venues)
    context = {
        "venues":match_venues
    }
    return render(request, 'api/Venues.html', context=context)
