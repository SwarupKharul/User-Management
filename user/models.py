from django.db import models

class User(models.Model):
    image = models.ImageField(upload_to='images/',default="default/default_user.png") 
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    email = models.EmailField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
