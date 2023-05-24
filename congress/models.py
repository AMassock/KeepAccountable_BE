from django.db import models

# Create your models here.
class API_KEYS(models.Model):
    site = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    key = models.CharField(max_length=250)

    def __str__(self):
        return self.site
    
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    login_name = models.CharField(max_length=25)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login_name
    
class FavoriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=250)

    def __str__(self):
        return self.item_name