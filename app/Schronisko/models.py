from django.db import models


# Create your models here.
class Zwierzak(models.Model):
    Imie = models.CharField(max_length=100)
    Rasa = models.CharField(max_length=100)
    DataPrzyjecia = models.DateField()
    StanyZdrowia = [('zdrowy'), ('chory'), ('w trakcie leczenia')]
    StanZdrowia = models.CharField(choices=StanyZdrowia, max_length=30, default='zdrowy')
    Opis = models.CharField(max_length=1000)

class Klient(models.Model):
    Imie = models.CharField(max_length=100)
    Nazwisko = models.CharField(max_length=100)
    AdresZamieszkania = models.CharField(max_length=12)
    NrTel = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)

class Rezerwacja(models.Model):
    Data = models.DateField()
    GodzinaOd = models.TimeField()
    GodzinaDo = models.TimeField()
    Zwierzak = models.ForeignKey(Zwierzak, on_delete=models.DO_NOTHING())
    Klient = models.ForeignKey(Klient, on_delete=models.DO_NOTHING())

class ProgramLojalnosciowy(models.Model):
    Punkty = models.IntegerField(max_length=5000)
    Klient = models.ForeignKey(Klient, on_delete=models.DO_NOTHING())

class Adopcja(models.Model):
    Data = models.DateField()
    Zwierzak = models.ForeignKey(Zwierzak, on_delete=models.DO_NOTHING())
    Klient = models.ForeignKey(Klient, on_delete=models.DO_NOTHING())

class Boks(models.Model):
    NrBoksu = models.IntegerField(max_length=100)
    Lokalizacja = models.CharField(max_length=300)
    Zwierzak = models.ForeignKey(Zwierzak, on_delete=models.DO_NOTHING())

class HistoriaLeczenia(models.Model):
    Data = models.DateField()
    Zwierzak = models.ForeignKey(Zwierzak, on_delete=models.DO_NOTHING())
    Opis = models.CharField(max_length=3000)
