from django.db import models

# Create your models here.

class booth(models.Model):
    polling_booth_number=models.IntegerField()
    polling_booth_name=models.CharField(max_length=100)
    parent_constituency=models.CharField(max_length=100)
    winner_2014=models.CharField(max_length=100)
    runnerup=models.CharField(max_length=100)
    margin_percente=models.FloatField()
    margin=models.IntegerField()
    total_voter=models.IntegerField()
    bjp_votes=models.IntegerField()
    bjp_percente_votes=models.FloatField()
    inc_votes=models.IntegerField()
    inc_percente_votes=models.FloatField()
    winner_2019=models.CharField(max_length=100)
    margin_percente_2=models.FloatField()
    margin_2=models.IntegerField()
    total_voter_2=models.IntegerField()
    bjp_votes_2=models.IntegerField()
    bjp_percente_votes_2=models.FloatField()
    inc_votes_2=models.IntegerField()
    inc_percente_votes_2=models.FloatField()
    class Meta:
        db_table ="main_table"

class TeamRegtration(models.Model):
    name=models.CharField(max_length=200) 
    nid=models.IntegerField()
    location=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name







