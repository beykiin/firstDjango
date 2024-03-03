from django.db import models

# Create your models here.
class Urunler(models.Model):
    urunResim=models.FileField(upload_to='urunResmi', null=True, blank=True)
    urunAdi=models.CharField(max_length=100,verbose_name="Ürün Adı: ")
    urunAciklamasi=models.TextField(max_length=500)
    fiyat=models.IntegerField(default=0)

    def __str__(self):
        return self.urunAdi