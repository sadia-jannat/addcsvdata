from django.contrib import admin

# Register your models here.
#admin.py
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from addcsvdataproject.models import test,booth

@admin.register(test)
class testAdmin(ImportExportModelAdmin):
     list_display = ("name","age")
     pass

@admin.register(booth)
class boothAdmin(ImportExportModelAdmin):
     list_display = ("polling_booth_number","polling_booth_name","parent_constituency","winner_2014","runnerup","margin_percente",
                     "margin","total_voter","bjp_votes","bjp_percente_votes","inc_votes","inc_percente_votes",
                     "winner_2019","margin_percente_2","margin_2","total_voter_2","bjp_votes_2","bjp_percente_votes_2",
                     "inc_votes_2","inc_percente_votes_2")
     pass
