# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

admin.site.site_header = "Python Testing"
admin.site.index_title = "Python Testing"

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
        path('', include('apps.core.urls')),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

# Debugger only in debug modes
# if settings.DEBUG:
#     urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
