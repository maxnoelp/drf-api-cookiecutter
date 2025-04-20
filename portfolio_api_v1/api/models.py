from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from filer.models import Image


class Skill(models.Model):
    name = models.CharField(_("Skill"), max_length=100)
    bs_icon = models.CharField(
        _("Bootstrap Icon"),
        max_length=100,
        help_text="Bootstrap icon name",
        blank=True,
    )
    image = FilerImageField(
        related_name=_("Image"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=100)
    teaser = RichTextField(blank=True)
    coding_language = models.CharField(max_length=100)
    coding_lang_icon = models.CharField(max_length=100, blank=True)
    description = RichTextField()
    images = models.ManyToManyField(Image, blank=True, related_name=_("Projektbilder"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Projekt")
        verbose_name_plural = _("Projekte")

    def __str__(self):
        return self.title
