"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from . import settings
from .views import counter, enum, gauge, histogram, home, summary
from django.conf.urls.static import static

urlpatterns = [
    path("", include("django_prometheus.urls")),
    path("", home, name="home"),
    path("counter/", counter, name="counter"),
    path("gauge/", gauge, name="gauge"),
    path("summary/", summary, name="summary"),
    path("histogram/", histogram, name="histogram"),
    path("enum/", enum, name="enum"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)