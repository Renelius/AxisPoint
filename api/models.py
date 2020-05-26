from django.db import models

class Items(models.Model):
    category=models.CharField(max_length=50)
    from_items=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    text=models.TextField(null=True, blank=True)
    thedate=models.DateField(db_index = True)
    id_items=models.IntegerField()

    def __str__(self):
        return self.category