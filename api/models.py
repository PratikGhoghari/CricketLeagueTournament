from django.db import models
from django.db.models.deletion import SET, SET_NULL
    
class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class Player(models.Model):
    ROLES = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All rounder", "All rounder")
    ]

    BATTING_HAND = [
        ("Left hand bat", "Left hand bat"),
        ("Right hand bat", "Right hand bat")
    ]

    BOWLING_HAND = [
        ("Left Arm Fast", "Left Arm Fast"),
        ("Right Arm Medium", "Right Arm Medium"),
        ("Right Arm Fast", "Right Arm Fast"),
        ("Left Arm Medium", "Left Arm Medium"),
        ("Right Arm Offbreak", "Right Arm Offbreak"),
        ("Left Arm Offbreak", "Left Arm Offbreak")
    ]

    player_name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    batting_hand = models.CharField(max_length=100, choices=BATTING_HAND, null=False)
    bowling_hand = models.CharField(max_length=100, choices=BOWLING_HAND, null=False)
    role = models.CharField(max_length=100, choices=ROLES, null=False)

    def __str__(self):
        return self.player_name
    
class Team(models.Model):
    name = models.CharField(max_length=100,blank=True)
    player = models.ManyToManyField(Player, related_name="Team_player_name", blank=True)
    country = models.ForeignKey(Country, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.player

class Match(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="team_id")
    opponent_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="opponent_team_id")
    match_date = models.DateField(auto_now=False)
    Venue = models.CharField(max_length=100)
    toss_win_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_toss_win_id")
    toss_lose_id = models.ForeignKey(Team, on_delete=models.CASCADE,related_name="team_toss_lose_id")
    match_win_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_match_win_id")
    match_lose_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_match_lose_id")
    man_of_match = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="man_of_match_id")
    bowler_of_match = models.ForeignKey(Player,on_delete=models.CASCADE, related_name="bowler_of_match_id")
    
    def __str__(self):
        return self.team_id.name + " " + self.opponent_id.name

