from django.db import models


# Create your models here.
class Zwierzak(models.Model):
    imie = models.CharField(max_length=100)
    rasa = models.CharField(max_length=100)
    data_przyjecia = models.DateField()
    stan_zdrowia = models.CharField( max_length=30, default='zdrowy')
    opis = models.CharField(max_length=1000)

class Klient(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    adres_zamieszkania = models.CharField(max_length=200)
    nr_tel = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)

class Rezerwacja(models.Model):
    data = models.DateField()
    godzina_od = models.TimeField()
    godzina_do = models.TimeField()
    zwierzak = models.ForeignKey(Zwierzak, on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)

class ProgramLojalnosciowy(models.Model):
    punkty = models.IntegerField
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)

class Adopcja(models.Model):
    data = models.DateField()
    zwierzak = models.ForeignKey(Zwierzak, on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)

class Boks(models.Model):
    nr_boksu = models.IntegerField
    lokalizacja = models.CharField(max_length=300)
    zwierzak = models.ForeignKey(Zwierzak, on_delete=models.CASCADE)

class HistoriaLeczenia(models.Model):
    data = models.DateField()
    zwierzak = models.ForeignKey(Zwierzak, on_delete=models.CASCADE)
    opis = models.CharField(max_length=3000)
