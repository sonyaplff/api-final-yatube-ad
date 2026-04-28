from django.db import models 
from django.contrib.auth import get_user_model 
 
User = get_user_model() 
 
class Group(models.Model): 
    title = models.CharField(max_length=200) 
 
class Post(models.Model): 
    text = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
 
class Comment(models.Model): 
    text = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
 
class Follow(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    following = models.ForeignKey(User, on_delete=models.CASCADE) 
