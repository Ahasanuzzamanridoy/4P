from django.db import models

# Create your models here.

class Receivebook(models.Model):
    BOOKID = models.CharField(max_length=6)
    FICODE = models.CharField(max_length=5)
    DATE = models.CharField(max_length=10)



    @staticmethod
    def get_all_Receivebooks():
        return Receivebook.objects.all()

    def __str__(self):
        return self.BOOKID

        return Receivebook.objects.all()

    def __str__(self):
        return self.FICODE

        return Receivebook.objects.all()

    def __str__(self):
        return self.DATE



