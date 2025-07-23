import random
import pytest
import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_EsperarCampo import EsperarCampoLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR

def test_verificar_elementos_ocultos(set_up_EsperarCampo):
    page = set_up_EsperarCampo # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    ecl = EsperarCampoLocatorPage(page)
    
    fg.verificar_texto_contenido(ecl.labelEspera, "Espera unos segundos", "verificar_texto_contenido_label", config.SCREENSHOT_DIR, 0)
    fg.validar_elemento_no_visible(ecl.campoNombre, "validar_elemento_no_visible_nombre", config.SCREENSHOT_DIR, 0)
    fg.validar_elemento_no_visible(ecl.campoApellido, "validar_elemento_no_visible_apellido", config.SCREENSHOT_DIR, 0)
    fg.validar_elemento_no_visible(ecl.comboBox, "validar_elemento_no_visible_comboBox", config.SCREENSHOT_DIR, 0)
    fg.validar_elemento_no_visible(ecl.termCondi, "validar_elemento_no_visible_términos_condiciones", config.SCREENSHOT_DIR, 0)
    
def test_visualizar_cada_campo(set_up_EsperarCampo):
    page = set_up_EsperarCampo # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    ecl = EsperarCampoLocatorPage(page)
    
    fg.verificar_texto_contenido(ecl.labelEspera, "Espera unos segundos", "verificar_texto_contenido_label", config.SCREENSHOT_DIR, 0)
    fg.rellenar_campo_de_texto(ecl.campoNombre, "Pedro", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR, 0)
    fg.validar_elemento_no_visible(ecl.comboBox, "validar_elemento_no_visible_comboBox", config.SCREENSHOT_DIR, 0)
    fg.validar_elemento_no_visible(ecl.termCondi, "validar_elemento_no_visible_términos_condiciones", config.SCREENSHOT_DIR, 0)
    
    fg.rellenar_campo_de_texto(ecl.campoApellido, "Camejo", "rellenar_campo_de_texto_apellido", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ecl.termCondi, "validar_elemento_no_visible_términos_condiciones", config.SCREENSHOT_DIR, 0)
    
    # Definición las opciones para ComboBox
    opciones_cb1 = ["1", "2", "3"]
    
    # Seleccionar una opción aleatoria directamente de la lista.
    # 'random.choice()' es ideal para elegir UN elemento aleatorio de una secuencia.
    # Es mucho más directo y legible que generar un número y luego mapearlo con 'if/elif'.
    valor_seleccionado_cb1 = random.choice(opciones_cb1)
    fg.seleccionar_opcion_por_valor(ecl.comboBox, valor_seleccionado_cb1, "seleccionar_opcion_por_valor_comboBox_uno", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ecl.menExitoso, "validar_elemento_no_visible_mensaje_exitoso", config.SCREENSHOT_DIR, 0)
    
    
def test_enviar_formulario_espera(set_up_EsperarCampo):
    page = set_up_EsperarCampo # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    ecl = EsperarCampoLocatorPage(page)
    
    fg.verificar_texto_contenido(ecl.labelEspera, "Espera unos segundos", "verificar_texto_contenido_label", config.SCREENSHOT_DIR, 0)
    fg.rellenar_campo_de_texto(ecl.campoNombre, "Pepito", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ecl.campoApellido, "Verde", "rellenar_campo_de_texto_apellido", config.SCREENSHOT_DIR)# Definición las opciones para ComboBox
    
    opciones_cb1 = ["1", "2", "3"]
    
    # Seleccionar una opción aleatoria directamente de la lista.
    # 'random.choice()' es ideal para elegir UN elemento aleatorio de una secuencia.
    # Es mucho más directo y legible que generar un número y luego mapearlo con 'if/elif'.
    valor_seleccionado_cb1 = random.choice(opciones_cb1)
    fg.seleccionar_opcion_por_valor(ecl.comboBox, valor_seleccionado_cb1, "seleccionar_opcion_por_valor_comboBox_uno", config.SCREENSHOT_DIR)
    
    fg.marcar_checkbox(ecl.termCondi,"marcar_checkbox_términos_condiciones", config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(ecl.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ecl.menExitoso, "Formulario enviado exitosamente", "verificar_texto_contenido_mensaje_exitoso", config.SCREENSHOT_DIR)