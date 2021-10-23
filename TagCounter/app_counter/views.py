from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import TagCounter
from .tasks import parse_url
from .service import not_found


class TagCounterPost(viewsets.ModelViewSet):

    @action(methods=['post'], detail=False)
    def url_parse_post(self, *args, **kwargs):
        url = self.request.data.get('url')
        if not url:
            return not_found()
        count_url = TagCounter(url=url)
        count_url.save()
        count_id = count_url.id
        parse_url.delay(count_id, url)
        return Response({'id': count_url.id})


class TagCounterGet(viewsets.ModelViewSet):

    @action(methods=['get'], detail=True)
    def url_parse_get(self, *args, **kwargs):
        count_id = self.kwargs.get('pk')
        count_url = TagCounter.objects.filter(id=count_id).first()
        if count_url:
            if count_url.status == 'done':
                return Response(count_url.tags)
            elif count_url.status == 'performed':
                return Response({'response': 'Please wait...'})
            elif count_url.status == 'error':
                return Response({'response': 'URL Error'})
        else:
            return not_found()
