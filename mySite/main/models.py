from django.db import models

# Create your models here.
class list_item(models.Model):
    name = models.CharField(max_length=100,blank= False, null=False, unique=True)
    added_to_cart = models.BooleanField(default=False)
    
    
    def __str__(self):
        return '{}'.format(self.name)
    
    
    
    class Meta:
        verbose_name_plural = 'items'
        verbose_name = "item"
    
    