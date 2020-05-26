from django.urls import path
from .views import items, send_xml, items_ajax, ajax_response

urlpatterns=[
    path('items', items),
    path('download', send_xml),
    path('ajax', items_ajax),
    path('ajax_response', ajax_response)
]