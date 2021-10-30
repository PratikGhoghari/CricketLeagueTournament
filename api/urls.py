from django.urls import path
from api import views

urlpatterns = [
    path('',views.home, name='home'),
    path('allteams/', views.get_all_teams, name='teams'),
    path('countries/', views.get_countries, name='countries'),                        # Done
    path('playerprofile/<int:pk>/', views.get_player_profile, name='playerprofile'),  # Done
    path('playerprofiles/', views.get_player_profiles, name='playerprofiles'),        # Done
    path('listofmatches/',views.get_all_matches, name='listofmatches'),               # Done
    path('matchsummary/<int:pk>/', views.get_match_summary, name='matchsummary'),   # Done
    path('matchsummaries/', views.get_all_match_summary, name='matchsummaries'),  # Done
    path('venues/',  views.get_venues, name='venues')                                 # Done
]
