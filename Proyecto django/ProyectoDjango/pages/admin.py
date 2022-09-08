from django.contrib import admin
from .models import Page
# Register your models here.

admin.site.register(Page)


#Configuración del panel
subtitle = "Panel de Gestión"
title = 'Proyecto con Django'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle