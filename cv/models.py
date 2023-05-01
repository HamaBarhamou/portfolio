from django.db import models


# Create your models here.
class Experience(models.Model):
    titre = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()

class Formation(models.Model):
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()

class Competence(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)

class CV(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    resume_professionnel = models.TextField()  # Champ pour le résumé professionnel
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    experiences = models.ManyToManyField(Experience)
    formations = models.ManyToManyField(Formation)
    competences = models.ManyToManyField(Competence)

    def __str__(self):
        return f"{self.prenom} {self.nom}"