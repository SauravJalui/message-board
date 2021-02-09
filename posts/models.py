from django.db import models

class Post(models.Model):
    '''This contains the data to be published as a post in the message board app'''
    text = models.TextField()

    def __str__(self):
        return self.text