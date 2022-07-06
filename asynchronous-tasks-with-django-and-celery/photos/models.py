from django.db import models


class Photo(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    updated_on = models.DateTimeField("Updated on", auto_now=True)  # TODO: Delete this? do I need this?
    title = models.CharField("Title", max_length=255)
    link = models.URLField(
        "Photo Link",
        max_length=255,
        help_text="The URL to the image page",
        # Assure unique links to avoid race conditions on Celery tasks
        unique=True,
    )
    image_url = models.URLField(
        "Image URL",
        max_length=255,
        help_text="The URL to the image file itself",
    )
    description = models.TextField("Description")

    class Meta:
        ordering = ["-created_on", "title"]

    def __str__(self):
        return self.title[:50]