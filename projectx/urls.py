"""projectx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include,re_path
from projectx.view import index,signup,activate,logout_request,signin,profil,settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from post.views import Posts, post_create, post_delete, Post1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('post/',include('post.urls')),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    path('logout/',logout_request,name='logout'),
    path('signin/',signin,name='signin'),
    path('signup/', signup,name='signup'),
    path('profil/', profil,name='profil'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',
                                                                 email_template_name='password_reset_email.html',
                                                                 subject_template_name='password_reset_subject.txt',
                                                                 success_url=reverse_lazy(
                                                                     'password_reset_done')
                                                                 ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                    success_url=reverse_lazy('password_reset_complete')),
            name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('settings/', settings,name='settings'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='base.html'),name='logout'),
    path('posts/', Posts, name="post-list"),
    path('<int:pk>/', Post1, name="post-details"),
    path("create/", post_create, name="post-create"),
    path("delete/<int:pk>/", post_delete, name="post-delete"),
    path("artykuly/", include("artykul.urls")),
]
