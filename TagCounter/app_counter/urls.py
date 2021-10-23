from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TagCounterGet, TagCounterPost

counter_post = TagCounterPost.as_view({
    'post': 'url_parse_post'
})

counter_get = TagCounterGet.as_view({
    'get': 'url_parse_get'
})

urlpatterns = format_suffix_patterns([
    path('tags/', counter_post),
    path('tags/<int:pk>', counter_get)
])
