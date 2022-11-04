import json

from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework_gis.pagination import GeoJsonPagination

from world import models
from world import serializers


class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        first_list = models.PhiladelphiaBusinessLicenses.objects.all()
        paginator = Paginator(first_list, 25)  # Show 25 contacts per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context["geometries"] = json.loads(serialize("geojson", page_obj))
        return context


class InvasivePlantViewSet(viewsets.ModelViewSet):
    queryset = models.InvasivePlant.objects.all()
    serializer_class = serializers.InvasivePlantSerializer
    pagination_class = GeoJsonPagination


@api_view(['GET'])
def get_map_stuff_api(request, *args, **kwargs):
    queryset = models.PhiladelphiaBusinessLicenses.objects.all()

    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return JsonResponse(json.loads(serialize("geojson", page_obj)))
