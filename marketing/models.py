from django.db import models

# Create your models here.
from django.utils.translation import gettext as _


class Signup(models.Model):
    """Model definition for Signup."""

    email = models.EmailField(_("email"), max_length=254)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Signup."""

        verbose_name = 'Signup'
        verbose_name_plural = 'Signups'

    def __str__(self):
        """Unicode representation of Signup."""
        return str(self.email)
