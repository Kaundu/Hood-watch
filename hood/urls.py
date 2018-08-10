from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^updateprofile$', views.updateprofile , name='updateprofile' ),
    url('^profile/(?P<user_id>\d+)', views.profile, name='profile'),
    url('^neighborhood/(?P<neighborhood_id>\d+)', views.neighborhood, name='neighborhood'),
    url('^business/(?P<business_id>\d+)' , views.business, name='business'),
]
# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)