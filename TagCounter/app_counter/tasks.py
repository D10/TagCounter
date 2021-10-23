from TagCounter.celery import app

from .models import TagCounter
from .parser import TagParser


@app.task
def parse_url(counter_id, url, status='done'):
    parser = TagParser(url)
    json_tags = parser.parse_tags
    if json_tags.get('Error'):
        status = 'error'
        json_tags = {}
    TagCounter.objects.filter(id=counter_id).update(status=status, tags=json_tags)
