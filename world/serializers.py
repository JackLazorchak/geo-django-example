from rest_framework_gis import serializers

from world import models


class InvasivePlantSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.InvasivePlant
        fields = ['id', 'objectid', 'site_id_fs', 'accepted_p', 'accepted_s', 'accepted_c', 'date_colle', 'total_area',
                  'infested_a', 'infested_p', 'fs_unit_na', 'crc_value']
        geo_field = 'geom'


class PhiladelphiaBusinessLicenseSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.PhiladelphiaBusinessLicenses
        fields = ['objectid', 'addressobj', 'address', 'unit_type', 'unit_num', 'zip', 'censustrac', 'parcel_id_field',
                  'opa_accoun', 'opa_owner', 'licensenum', 'revenuecod', 'licensetyp', 'rentalcate', 'initialiss',
                  'mostrecent', 'expiration', 'inactiveda', 'licensesta', 'numberofun', 'owneroccup', 'legalfirst',
                  'legallastn', 'legalname', 'legalentit', 'business_n', 'business_m', 'ownerconta', 'ownercon_1',
                  'ownercon_2', 'ownercon_3', 'ownercon_4', 'ownercon_5', 'ownercon_6', 'ownercon_7', 'ownercon_8',
                  'ownercon_9', 'geocode_x', 'geocode_y', 'council_di', 'posse_jobi'
                  ]
        geo_field = 'geom'
