from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login$',views.UserAuthentication),
    url(r'^logout$',views.Logout),
    url(r'^register$',views.Register),
    url(r'^key$',views.GetPublicKey),
    url(r'^info$',views.UserInfo)
]