from django.contrib import admin
from . models import *

from import_export.admin import ImportExportModelAdmin


# Register your models here.
class eventModel(ImportExportModelAdmin):
    list_display = ["__str__", "date"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = event
admin.site.register(event, eventModel)


class liveModel(ImportExportModelAdmin):
    list_display = ["__str__", "date"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = live
admin.site.register(live, liveModel)


class pageModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = page
admin.site.register(page, pageModel)


class teamModel(ImportExportModelAdmin):
    list_display = ["__str__", "role"]
    list_filter = ["role"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = teamProfile
admin.site.register(teamProfile, teamModel)


class memeModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = meme
admin.site.register(meme, memeModel)


class quoteModel(ImportExportModelAdmin):
    list_display = ["__str__", "author"]
    list_per_page = 25
    search_fields = ["__str__", "author"]
    class Meta:
        Model = quote
admin.site.register(quote, quoteModel)
