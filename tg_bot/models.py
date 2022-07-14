from django.db import models



class KelganTime(models.Model):
    user = models.CharField(max_length=25)
    kelgan_vaqt  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class KetganVaqt(models.Model):
    user = models.CharField(max_length=25)
    ketgan_vaqt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user







# Create your models here.
