from django.db import models

# Create your models here.
class article(models.Model):
    id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=50)
    article_author = models.CharField(max_length=20, default='moo')
    article_type = models.CharField(max_length=20,default='null')
    article_date = models.DateTimeField('date published')
    article_text = models.TextField(null=False)
    article_views = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + '.' + self.article_title


