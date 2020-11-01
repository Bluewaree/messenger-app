from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Message(models.Model):
    username = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.message}"

    def save(self, **kwargs):
        if self.message is None or self.username is None:
            raise ValidationError(_("Message and username fields must be valid"))

        return super().save(**kwargs)
