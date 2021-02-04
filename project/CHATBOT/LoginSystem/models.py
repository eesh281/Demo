from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    image = models.ImageField()

    if full_name == "" or user_name == "" or email == "" or password == "":
        raise ValidationError("one of the above field is empty")

    def __str__(self):
        return self.user_name
    

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE
            )

    if message == '':
        raise ValidationError("message can never be empty")

    def __str__(self):
        return self.user+"_"+str(id)

    

        
    
