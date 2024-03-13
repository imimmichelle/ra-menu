from django import template
from django.db.models import Q
register = template.Library()

@register.filter
def desire(preferences, desire):
    return preferences.filter(desire=desire)

@register.filter
def user(preferences, user):
    return preferences.filter(user=user)

@register.filter
def code(preferences, code):
    return preferences.filter(code=code)

@register.filter
def not_user(preferences, user):
    return preferences.filter(~Q(user=user))

@register.filter
def category(desires, cat):
    return desires.filter(category=cat)

#register.filter('desire_user', desire_user)

