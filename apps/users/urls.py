from django.urls import path
# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [

    #Usuarios
    path('sign-up/', views.SignUp.as_view(), name = 'signup'),
    path('accounts/login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('users/change_password/', login_required(views.ChangePassword.as_view()), name='update_password'),
    path('perfil/<int:pk>/', login_required(views.detailUserRegister), name='perfil'),
    path('docente/',login_required(views.listDocente),name='docente'),
    path('estudiante/',login_required(views.listEstudiante),name='estudiante'),
    path('usuario/',login_required(views.listUsuario),name='usuario'),
    path('rol/',login_required(views.listRol),name='list_rolPermiso'),
    path('permiso/',login_required(views.listPermiso),name='permiso'),
    path('puesto/',login_required(views.listPuesto), name='puesto'),
    path('user/add',login_required(views.crearUsuario.as_view()), name='add_user'),
    path('user/delete/<int:pk>',login_required(views.deleteUser), name='delete_user'),
    path('user/detail/<int:pk>',login_required(views.detailUser), name='detail_user'),
    path('user/update/<int:pk>',login_required(views.UpdateUser.as_view()), name='update_user'),

    #Roles
    
    path('rol/crear/', login_required(views.RolCreate.as_view()), name='CrearRol'),
    path('rol/actualizar/<int:pk>/', login_required(views.RolUpdate.as_view()), name='ActualizarRol'),
    path('rol/eliminar/<int:pk>/', login_required(views.RolDelete.as_view()), name='EliminarRol'),

    #Permisos
    
    path('permiso/crear/', login_required(views.PermisoCreate.as_view()), name='CrearPermiso'),
    path('permiso/actualizar/<int:pk>/', login_required(views.PermisoUpdate.as_view()), name='ActualizarPermiso'),
    path('permiso/eliminar/<int:pk>/', login_required(views.PermisoDelete.as_view()), name='EliminarPermiso'),


]