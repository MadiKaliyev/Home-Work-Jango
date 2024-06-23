from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include('bboard.urls')),  
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')), 
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),  
    path('todo/', include(('todo.urls', 'todo'), namespace='todo')),  
    path('blog/', include('blog.urls')),   
]
