from django_filters import rest_framework as filters

from docstore.models import Folder


class FolderFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    topic = filters.CharFilter(
        field_name="documents__topic__name", lookup_expr="icontains"
    )
    document = filters.CharFilter(field_name="documents__name", lookup_expr="icontains")

    class Meta:
        model = Folder
        fields = ["name", "document", "topic"]
