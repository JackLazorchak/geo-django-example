from django.contrib.gis import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import WorldBorder, MontgomeryCountyParcel, MontgomeryCountyGeology, MontgomeryCountyWatershed, \
    InvasivePlant, PhiladelphiaBusinessLicenses


class MontgomeryCountyParcelAdmin(GISModelAdmin):
    search_fields = ['addr1', 'addr2', 'addr3']
    list_display = ['addr1', 'addr2', 'addr3']
    ordering = ['-created_da']


class MontgomeryCountyGeologyAdmin(GISModelAdmin):
    search_fields = ['unit_name']
    list_display = ['unit_name']
    ordering = ['unit_name']


class MontgomeryCountyWatershedAdmin(GISModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    ordering = ['name']


class InvasivePlantAdmin(GISModelAdmin):
    search_fields = ['accepted_p', 'accepted_s', 'accepted_c', 'fs_unit_na']
    list_display = ['accepted_p', 'accepted_s', 'accepted_c', 'fs_unit_na']
    ordering = ['-date_colle']


class PhiladelphiaBusinessLicensesAdmin(GISModelAdmin):
    search_fields = ['address']
    list_display = ['address']


admin.site.register(WorldBorder, GISModelAdmin)
admin.site.register(InvasivePlant, InvasivePlantAdmin)
admin.site.register(MontgomeryCountyParcel, MontgomeryCountyParcelAdmin)
admin.site.register(MontgomeryCountyGeology, MontgomeryCountyGeologyAdmin)
admin.site.register(MontgomeryCountyWatershed, MontgomeryCountyWatershedAdmin)
admin.site.register(PhiladelphiaBusinessLicenses, PhiladelphiaBusinessLicensesAdmin)