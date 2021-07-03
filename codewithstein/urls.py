from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import *

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('addsoru/', createSoru, name="create_soru"),
    path('<slug:slug>/', post_detail, name='post_detail'),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
