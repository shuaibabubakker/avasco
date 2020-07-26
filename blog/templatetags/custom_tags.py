from ..models import Committee
from django import template

register = template.Library()

@register.simple_tag
def president():
      president_no = Committee.objects.first().president.phone_1_india
      
      return  president_no

@register.simple_tag
def secretary():
      secretary_no = Committee.objects.first().secretary.phone_1_india
      
      return secretary_no
