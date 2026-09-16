from django.db import models

#choices to be used in sex and place of death models
SEX_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]

PLACE_OF_DEATH_CHOICES = [
    ("Hospital", "Hospital"),
    ("Home", "Home"),
    ("Other", "Other"),
]

# My models start here.
class VerbalAutopsy(models.Model):
    deceased_name = models.CharField(max_length = 120)
    sex = models.CharField(max_length = 1, choices = SEX_CHOICES)
    age_at_death = models.IntegerField()
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length = 100, choices = PLACE_OF_DEATH_CHOICES)
    respondent_name = models.CharField(max_length = 120)
    respondent_relationship = models.CharField(max_length = 50)
    interview_date = models.DateField()
    symptoms = models.TextField()
    probable_cause_of_death = models.CharField(max_length = 100, blank = True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.deceased_name
