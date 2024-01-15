from django.db import models
from django.utils import timezone


class AlcoInfo(models.Model):
    title = models.CharField(
        verbose_name="Name",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Description",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    expired = models.DateTimeField(
        verbose_name="Date and time of expiration",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )
    qr_image = models.ImageField(
        verbose_name="Date and time of expiration",
        db_index=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to='alco_links'
    )

    class Meta:
        app_label = "django_app"
        ordering = (
            "expired",
            "-title",
        )
        verbose_name = "Alco"
        verbose_name_plural = "Alcos"

    def __str__(self):
        return f"<Alco {self.title}({self.id})/ >"
