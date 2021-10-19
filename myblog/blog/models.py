# A model is the single, definitive source of information about your data. 
# It contains the essential fields and behaviors of the data you’re storing. 
# Generally,each model maps to a single database table.

# Each attribute of the model represents a database field.

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

# function __str__ is defining the title of the blog (returns title of the class)
    def __str__(self):
        return self.title
