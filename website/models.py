from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)# 2024-01-06 07:17:32.429784
                                                      # 2024-01-06 07:20:15.293047
                                                      
    class Meta:
        ordering =['-create_date']
                                                          
    def __str__(self):
        return self.name                                                  
                                                      
# Select * from  post
# select * from post where status = 1