from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/download-pdf/', views.download_pdf_rekap_hari_ini, name='download_pdf_rekap'),
    path('admin-panel/download-excel/', views.download_excel_rekap_hari_ini, name='download_excel_rekap'),
    path('ocr/process/', views.ocr_process_image, name='ocr_process'),
    path('admin-panel/profile/', views.admin_profile_view, name='admin_profile'),
    # Route untuk testing 404 (dapat dihapus di production)
    path('test-404/', views.test_404, name='test_404'),
    # Catch-all untuk menampilkan custom 404 (harus di akhir)
    re_path(r'^.*$', views.custom_404),
]

