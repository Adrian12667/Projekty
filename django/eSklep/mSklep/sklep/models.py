from django.db import models
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=200,
                            db_index=True)
    etykieta = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    class Meta:
        ordering = ('nazwa',)
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'
    def __str__(self):
        return self.nazwa
class Produkt(models.Model):
    kategoria = models.ForeignKey(Kategoria,
                                 related_name='produkty',
                                 on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=200, db_index=True)
    etykieta = models.SlugField(max_length=200, db_index=True)
    obraz = models.ImageField(upload_to='produkty/%Y/%m/%d',
                              blank=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostepne = models.BooleanField(default=True)
    utworzono = models.DateTimeField(auto_now_add=True)
    aktualizacja = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('nazwa',)
        verbose_name = 'produkt'
        verbose_name_plural = 'produkty'
        index_together = (('id', 'etykieta'),)
    def __str__(self):
        return self.nazwa


