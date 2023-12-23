from django.contrib import admin
from django.urls import path

from things.views import thing_list, thing_retrieve, thing_create, thing_update, thing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', thing_list),
    path('things/<pk>', thing_retrieve),
    path('things/<pk>/edit/', thing_update),
    path('add-thing/', thing_create),
    path('things/<pk>/delete/', thing_delete)
]
