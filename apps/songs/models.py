from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import transaction


# Create your models here.
class Song(models.Model):
    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")
        ordering = ["name"]

    name = models.CharField(
        max_length=100,
        verbose_name=_("Song Name"),
        help_text=_("Enter the name of the song"),
    )

    def __str__(self):
        return self.name

    @transaction.atomic
    def test_atomicity(self):
        self.name = "Test atomicity"
        self.save()

        raise Exception("Changes will not be saved")


class Playlist(models.Model):
    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")
        ordering = ["name"]

    name = models.CharField(
        max_length=100,
        verbose_name=_("Playlist Name"),
        help_text=_("Enter the name of the playlist"),
    )
    songs = models.ManyToManyField(
        Song,
        through="Element",
        related_name=_("playlist"),
        verbose_name=_("Songs"),
        help_text=_("Select the songs for the playlist"),
    )

    def __str__(self):
        return self.name


class Element(models.Model):
    class Meta:
        verbose_name = _("Element")
        verbose_name_plural = _("Elements")
        ordering = ["position"]

    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.CASCADE,
        related_name=_("element"),
        verbose_name=_("Playlist"),
        help_text=_("Select the playlist"),
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name=_("element"),
        verbose_name=_("Song"),
        help_text=_("Select the song"),
    )
    position = models.IntegerField(
        verbose_name=_("Position"),
        help_text=_("Enter the position of the song in the playlist"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.playlist.name} - {self.song.name}"
