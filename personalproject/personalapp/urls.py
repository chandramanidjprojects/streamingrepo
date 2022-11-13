from django.urls import path,include,re_path
from personalapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [

    path('',views.wellcomepage),
    path('update_profile/',views.update_profile),
    path('post_likes/',views.likes,name='likes'),
    path('post_comments/<int:id>/',views.post_comments),
    path('post_comments/',views.post_comments,name='comments'),
    path('create_post',views.create_post),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('accounts/',include('django.contrib.auth.urls')),
]
