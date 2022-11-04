from rest_framework_gis import serializers

from world import models


class InvasivePlantSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.InvasivePlant
        fields = ['id', 'objectid', 'site_id_fs', 'accepted_p', 'accepted_s', 'accepted_c', 'date_colle', 'total_area',
                  'infested_a', 'infested_p', 'fs_unit_na', 'crc_value']
        geo_field = 'geom'
