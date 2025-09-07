from django.db import models
import os


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name must be unique
    code = models.CharField(max_length=100, unique=True)  # Code must be unique
    category = models.CharField(max_length=100, blank=True, null=True)  # Add this line

    # Image fields for storing up to 10 images
    image1 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image7 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image8 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image9 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    image10 = models.ImageField(upload_to='recipes/images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete image files when the recipe is deleted
        for image_field in [
            self.image1, self.image2, self.image3, self.image4, self.image5,
            self.image6, self.image7, self.image8, self.image9, self.image10
        ]:
            if image_field and os.path.isfile(image_field.path):
                os.remove(image_field.path)
        super().delete(*args, **kwargs)
