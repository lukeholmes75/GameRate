from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=128, unique=True)
    publisher = models.CharField(max_length=128)
    game_Description = model.CherField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    story_rating = models.IntegerField(default = 0)
    gameplay_rating = models.IntegerField(default = 0)
    graphics_rating = models.IntegerField(default = 0)
    difficulty_rating = models.IntegerField(default = 0)
    picture = models.ImageField(upload_to='game_images', blank=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_lenght=128, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name