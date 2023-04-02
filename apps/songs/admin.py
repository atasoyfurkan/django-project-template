from django.contrib import admin
from apps.songs.models import Song, Playlist, Element


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("name",)
    actions = ("test_atomicity",)

    @admin.action(description="Test atomicity")
    def test_atomicity(self, request, queryset):
        for song in queryset:
            song.test_atomicity()


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ("get_songs",)

    @admin.display(description="Songs")
    def get_songs(self, obj):
        return "\n".join([s.name for s in obj.songs.all()])


admin.site.register(Element)
