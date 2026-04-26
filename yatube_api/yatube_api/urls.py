from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import include, path
from django.views.generic import TemplateView
>>>>>>> 44e7ce60e9f815f6f18663d3eb4b27fb03f32c47

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
<<<<<<< HEAD
]
=======
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

>>>>>>> 44e7ce60e9f815f6f18663d3eb4b27fb03f32c47
