from django.urls import path

from table import views

actions_url = {'actions': {'get': 'list', 'post': 'create'}}
actions_obj = {'actions': {'delete': 'destroy'}}

urlpatterns = [
    # Your URLs...
    path('', views.TableViewSet.as_view(**actions_url), name='tables'),
    path(r'<table_id>', views.TableViewSet.as_view(**actions_obj), name='tables')
]
