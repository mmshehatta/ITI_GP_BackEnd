from django.db import models
from users.models import User
from offers.models import Offer


# Create your models here.

class Need(models.Model):
    # name = models.CharField(max_length=100 , null=False , blank=False , unique=True)
    # id by default exists

    # Relation with users by user_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Relation with offers by offer_id
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name