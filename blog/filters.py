import django_filters
from django_filters import DateFilter, CharFilter

from .models import Member


class MemberFilter(django_filters.FilterSet):

    note1= CharFilter(field_name='name' , lookup_expr='icontains')
    note2= CharFilter(field_name='country' , lookup_expr='icontains')
    note3= CharFilter(field_name='city' , lookup_expr='icontains')
    note4= CharFilter(field_name='place' , lookup_expr='icontains')
    note5= CharFilter(field_name='occupation_or_course' , lookup_expr='icontains')
    note6= CharFilter(field_name='company_or_institution_name' , lookup_expr='icontains')
    note7= CharFilter(field_name='company_or_institution_place' , lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['blood_group', 'section', 'sex']
