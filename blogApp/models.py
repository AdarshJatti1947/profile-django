from django.db import models

# Create your models here.

class Blog_title(models.Model):
    post_title=models.TextField(max_length=20)
    post1=models.TextField(max_length=1000,null=True)

    def __str__(self):
        return f"{self.post_title} - {self.post1}"



#class Blog_post(models.Model):
#    post = models.TextField(max_length=2000)

#    def __str__(self):
#        return self.post


