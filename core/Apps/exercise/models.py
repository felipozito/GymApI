from django.db import models

# Create your models here.
class Exercise(models.Model):
    MUSCLE_GROPUS = (
        ('Pecho', 'Pecho'),
        ('Espalda', 'Espalda'),
        ('Piernas', 'Piernas'),
        ('Hombros', 'Hombros'),
        ('Brazos', 'Brazos'),
        ('Abdomen', 'Abdomen'),
    )
    DIFICULTY = (
        ('Facil', 'Facil'),
        ('Medio', 'Medio'),
        ('Dificil', 'Dificil')
    )
    
    id=models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
   #image = models.ImageField(upload_to='exercise_images/')
    #video = models.FileField(upload_to='exercise_videos/')
    difficulty = models.CharField(max_length=50 , choices=DIFICULTY , blank=True)
    muscle_group = models.CharField(max_length=50 , choices=MUSCLE_GROPUS)
    equipment = models.CharField(max_length=50 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name