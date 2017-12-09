"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
# Use static() to add url mapping to serve static files (like CSS, JS and images by default) during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from signuppage import views as signup_view
import catalog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^signup/$', catalog_views.signup, name='signup'),
    # for sign up
    url(r'^books/',include('userbook.urls')),

    url(r'^storemanager/', include('storemanager.urls')),

    url(r'^signup/$', signup_view.signup),
    url(r'^accounts/login', catalog.views.login_user, name='login'),
    url(r'^accounts/signup', catalog.views.signup_user),
    url(r'^accounts/logout', catalog.views.logout_user,name='logout'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

