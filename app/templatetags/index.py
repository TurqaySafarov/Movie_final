from django import template
import datetime
from django.utils import timezone

register = template.Library()

@register.filter(name='multiply')
def add1(value):
    """Multiplies the value by the argument."""
    try:
        return value+1 
    except (ValueError, TypeError):
        return value
    


@register.filter(name='duration_format')
def duration_format(value):
    """Format a timedelta object (DurationField) as 'HH:MM:SS'."""
    total_seconds = int(value.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02} hours {minutes:02} minutes'



@register.filter(name='getfilename')
def filename(value):
    
    name = value.split('/')[-1]
    return name



@register.filter(name='decreaseword')
def decreaseword(value):
    
    name = ' '.join(value.split(' ')[:10])+'...'
    return name



@register.filter(name='decreaseword1')
def decreaseword1(value):
    
    name = ' '.join(value.split(' ')[:30])+'...'
    return name





@register.filter(name='time_diff')
def time_diff(value):
    """
    Calculate the time difference between the given datetime and now.
    Example: 2024-10-02 20:20 -> '3 hours ago'
    """
    if not isinstance(value, datetime.datetime):
        return value

    now = timezone.now()

    # Make sure the value is timezone-aware (if necessary)
    if timezone.is_aware(value):
        diff = now - value
    else:
        diff = now - timezone.make_aware(value, timezone.get_default_timezone())

    # Calculate difference in seconds
    seconds = diff.total_seconds()

    # Calculate time difference and return human-readable format
    if seconds == 0:
        return "just now"
    elif seconds < 60:
        return f"{int(seconds)} second{'s' if seconds > 1 else ''} ago"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds // 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif seconds < 2592000:
        days = int(seconds // 86400)
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        months = int(seconds // 2592000)
        return f"{months} month{'s' if months > 1 else ''} ago"