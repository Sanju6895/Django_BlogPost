from django.db import models
from PIL import Image


# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profiles_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #Overiding function save to make pics smaller in size so they can be loaded faster
    #Commet this code because we are using AWS and if you want to resize pics there
    #make use of lambda function
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 and img.width > 300:
    #         output_size =  (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)