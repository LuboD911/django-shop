from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('bestshop.products.urls')),
    path('accounts/',include('bestshop.accounts.urls')),
    path('more/',include('bestshop.footer.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
