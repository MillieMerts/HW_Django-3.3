from django_filters import DateFromToRangeFilter, FilterSet, BaseInFilter
from .models import Advertisement


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()
    status = BaseInFilter(field_name='status')

    class Meta:
        model: Advertisement
        fields = ['created_at', 'status']