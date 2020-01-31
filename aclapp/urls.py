from django.urls import path
from .views import alertUnreactedView, alertPending, alertClosed_user,alertClosed_staff, alertUnreactedApi, ApiView, acl_update, registerPage, loginPage, logoutUser
#from .apiview import alertUnreactedApi, ApiView

urlpatterns = [
    path('', alertUnreactedView, name='unreacted'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    #path('',searchAlert, name='search' ),
    path('api/', ApiView.as_view(), name='table'),
    path('pending/', alertPending, name='pending'),
    path('regularised/', alertClosed_user, name='regularised'),
    path('regularised-staff/', alertClosed_staff, name='regularised_staff'),
    path('<int:id>/update', acl_update, name='response'),
    path('api/unreacted/', alertUnreactedApi, name='unreactedApi')
]