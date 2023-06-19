from django.contrib import admin
from . models import category, article, comment, Report, FeaturedPost

from import_export.admin import ImportExportModelAdmin


class categoryModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = category
admin.site.register(category, categoryModel)


class articleModel(ImportExportModelAdmin):
    list_display = ["__str__", "author", "category", "posted_on"]
    list_filter = ["posted_on", "category"]
    list_per_page = 25
    search_fields = ["__str__", "details"]
    class Meta:
        Model = article
admin.site.register(article, articleModel)


class FeaturedPostModel(ImportExportModelAdmin):
    list_display = ["__str__", "post", "position"]
    list_filter = ["post", "position"]
    list_per_page = 3
    search_fields = ["__str__", "post"]
    class Meta:
        Model = FeaturedPost
admin.site.register(FeaturedPost, FeaturedPostModel)


class commentModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = comment
admin.site.register(comment, commentModel)


class reportModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    class Meta:
        Model = Report
admin.site.register(Report, reportModel)



