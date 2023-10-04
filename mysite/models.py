from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200) 
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)  #日期 時間(自動取得)
    
    class Meta:
        ordering=('-pub_date', ) #,強制新增combo
        
    def __str__(self) -> str:
        return self.title