from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100 , verbose_name='İsim Soyisim')
    email = models.EmailField(max_length=254,blank=True,verbose_name='E Posta')
    phone = models.CharField(max_length=254 , verbose_name='Telefon')
    message = models.TextField(verbose_name='Açıklama',blank=True)
    isRead = models.BooleanField(default=False,verbose_name='Okundu mu?')
    created= models.DateTimeField(auto_now_add= True, verbose_name="Oluşturulma Tarihi")


    def __str__(self):
        return self.name
    class Meta:
        managed = True
        verbose_name = 'İletişim Formu'
        verbose_name_plural = 'İletişim Formu'