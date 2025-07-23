import random
import pytest
import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from playwright.sync_api import expect
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_DragDrop import DragDropLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR

def test_elementos_presentes(set_up_DragDrop):
    page = set_up_DragDrop # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    ddl = DragDropLocatorPage(page)
    
    fg.validar_elemento_visible(ddl.botonRefrescarPag, "validar_elemento_visible_botón_refrescar", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ddl.objDrag, "validar_elemento_visible_objeto_drag", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ddl.objDrop, "validar_elemento_visible_objeto_drop", config.SCREENSHOT_DIR)

@pytest.mark.xfail(reason="Fallo intermitente de Drag & Drop en Firefox debido a timeout en hover.")    
def test_hacer_drag_drop(set_up_DragDrop):
    page = set_up_DragDrop # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    ddl = DragDropLocatorPage(page)
    
    fg.realizar_drag_and_drop(ddl.objDrag, ddl.objDrop, "DragAndDrop_exitoso", config.SCREENSHOT_DIR)
    fg.verificar_alerta_simple_con_expect_event(ddl.objDrop, "Prueba exitosa", "Alerta_Prueba_Exitosa", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ddl.objDrop.filter(has_text="Arrástrame"), "Arrastrame_dentro_Soltar_aqui", config.SCREENSHOT_DIR)

@pytest.mark.xfail(reason="Fallo intermitente de Drag & Drop en Firefox debido a timeout en hover.")    
def test_refrescar_pagina(set_up_DragDrop):
    page = set_up_DragDrop  # 'page' es el objeto Page de Playwright

    fg = Funciones_Globales(page)
    ddl = DragDropLocatorPage(page)
    
    fg.realizar_drag_and_drop(ddl.objDrag, ddl.objDrop, "DragAndDrop_exitoso", config.SCREENSHOT_DIR)
    fg.verificar_alerta_simple_con_expect_event(ddl.objDrop, "Prueba exitosa", "Alerta_Prueba_Exitosa", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ddl.objDrop.filter(has_text="Arrástrame"), "Arrastrame_dentro_Soltar_aqui", config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(ddl.botonRefrescarPag, "hacer_click_en_elemento_botón_refrescar", config.SCREENSHOT_DIR)
    
    # Se espera que el DOM esté completamente cargado y la red inactiva.
    fg.page.wait_for_load_state('domcontentloaded')
    fg.page.wait_for_load_state('networkidle')
    
    # Verificar que el área "Soltar aquí" tiene solo su texto original
    fg.verificar_texto_contenido(ddl.objDrop, "Soltar aquí", "Soltar_aqui_reestablecido", config.SCREENSHOT_DIR)
    
    # Verificar que el elemento "Arrastrame" NO está dentro del "Soltar aquí"
    # ¡Línea ajustada para usar el localizador 'objDrag' directamente dentro de 'objDrop'! 👇
    expect(ddl.objDrop.locator(ddl.objDrag)).not_to_be_visible()
    