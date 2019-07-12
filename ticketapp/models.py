from django.db import models

#Model saving ticket data
class Ticket(models.Model):
    ticket=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name
