from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title = 'Pastebin API')

app_name= 'PMO'
urlpatterns = [
	path('',views.index, name = 'index'),
	path('<int:case_id>/',views.detail,name='detail'),
	path('<int:case_id>/authorisation/',views.authorise,name='authorise'),
	url(r'^cases/$',views.CaseList.as_view()),
	url(r'^cases/(?P<pk>[0-9]+)/$',views.CaseDetail.as_view()),
	url(r'^$', views.api_root),
	url(r'^schema/$', schema_view),
]