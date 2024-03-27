from django.db import models


from django.db import models

class FeedBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)  # Corrected typo here
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "FeedBack"

