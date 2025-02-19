import datetime
from django import template

register = template.Library()

@register.filter
def timestamp_to_date(value):
    """Negativ yoki pozitiv timestampni inson o‘qiy oladigan formatga aylantiradi."""
    try:
        dt = datetime.datetime.fromtimestamp(int(value))
        return dt.strftime('%d.%m.%Y')
    except (ValueError, TypeError):
        return "Noto‘g‘ri timestamp"
