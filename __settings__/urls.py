from django.contrib             import  admin
from django.urls                import  path, include
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls'))
]

# для раздачи статических файлов картинок и прочее для dev режима.
urlpatterns += static(settings.MEDIA_URL, documet_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, documet_root=settings.STATIC_ROOT)

