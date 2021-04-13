from django.contrib import admin
from . models import category, article, comment, Report, Withdraw

# Register your models here.
# class authorModel(admin.ModelAdmin):
#     list_display = ["__str__"]
#     list_per_page = 25
#     search_fields = ["__str__"]
#     class Meta:
#         Model = author
# admin.site.register(author, authorModel)

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


class withdrawModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    list_filter = ['payment_done',]
    class Meta:
        Model = Withdraw
admin.site.register(Withdraw, withdrawModel)
