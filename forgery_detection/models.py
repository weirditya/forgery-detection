from django.db import models

# Create your models here.
class database(models.Model): 
    Please_Select_Image_to_Detect_Forgery = models.ImageField(upload_to='input_images/')
    def __str__(self):
        return str(self.Please_Select_Image_to_Detect_Forgery)