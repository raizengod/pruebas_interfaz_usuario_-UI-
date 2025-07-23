import pytest
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_barraNavegacion import BarraNavLocatorPage
from PRV.locator.locator_AccionBoton import AccionBotonLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR 
    
def test_hacer_click_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(abl.botonClick, "hacer_click_en_elemento", config.SCREENSHOT_DIR, None)
    fg.verificar_texto_contenido(abl.menExitoso, "Has hecho clic en el botÃ³n pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
    
def test_hacer_doble_click_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_doble_click_en_elemento(abl.botonDobleClick, "hacer_doble_click_en_elemento", config.SCREENSHOT_DIR, None)
    fg.verificar_texto_contenido(abl.menExitoso, "Has hecho doble clic en el botÃ³n pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_hover_over_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_hover_en_elemento(abl.botonHoverOver, "hacer_hover_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has pasado el cursor sobre el botÃ³n pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_right_click_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_derecho_en_elemento(abl.botonRightClick, "hacer_click_derecho_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has hecho clic derecho en el botÃ³n pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_mouse_down_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_mouse_down_en_elemento(abl.botonMouseDown, "hacer_mouse_down_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has presionado el botÃ³n del ratÃ³n pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_mouse_up_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_mouse_down_en_elemento(abl.botonMouseUp, "hacer_mouse_up_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has liberado el botÃ³n del ratÃ³n pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_focus_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_focus_en_elemento(abl.botonFocus, "hacer_focus_en_elemento_boton_Focus", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "El botÃ³n tiene foco pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
@pytest.mark.xfail(reason="Comportamiento atipico en webkit")
def test_hacer_blur_sin_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(abl.botonBlur, "hacer_click_en_elemento_boton_blur", config.SCREENSHOT_DIR, None)
    fg.hacer_blur_en_elemento(abl.botonBlur, "hacer_blur_en_elemento_botón_fucos", config.SCREENSHOT_DIR)
    fg.mouse_mueve_y_hace_clic_xy(100, 100, "mouse_mueve_y_hace_clic_x100_y100", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "El botÃ³n ha perdido el foco pero el campo no es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.verificar_texto_contenido(abl.menError, "El campo no puede estar vacÃ­o.", "verificar_texto_contenido_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_click_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo click", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(abl.botonClick, "hacer_click_en_elemento", config.SCREENSHOT_DIR, None)
    fg.verificar_texto_contenido(abl.menExitoso, "Has hecho clic en el botÃ³n y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_doble_click_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo doble click", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_doble_click_en_elemento(abl.botonDobleClick, "hacer_doble_click_en_elemento", config.SCREENSHOT_DIR, None)
    fg.verificar_texto_contenido(abl.menExitoso, "Has hecho doble clic en el botÃ³n y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_hover_over_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo hover over", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_hover_en_elemento(abl.botonHoverOver, "hacer_hover_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has pasado el cursor sobre el botÃ³n y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_right_click_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo right click", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_derecho_en_elemento(abl.botonRightClick, "hacer_click_derecho_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has hecho clic derecho en el botÃ³n y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_mouse_down_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo mouse down", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_mouse_down_en_elemento(abl.botonMouseDown, "hacer_mouse_down_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has presionado el botÃ³n del ratÃ³n y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_mouse_up_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo mouse up", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_mouse_down_en_elemento(abl.botonMouseUp, "hacer_mouse_up_en_elemento", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "Has liberado el botÃ³n del ratÃ³n y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
def test_hacer_focus_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo focus", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_focus_en_elemento(abl.botonFocus, "hacer_focus_en_elemento_boton_Focus", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "El botÃ³n tiene foco y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
@pytest.mark.xfail(reason="Comportamiento atipico en webkit")    
def test_hacer_blur_con_nombre(set_up_AccionBoton):
    page = set_up_AccionBoton # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'BarraNavLocatorPage'
    abl = AccionBotonLocatorPage(page)
    
    fg.rellenar_campo_de_texto(abl.campoNombre, "haciendo blur", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(abl.botonBlur, "hacer_click_en_elemento_boton_blur", config.SCREENSHOT_DIR, None)
    fg.hacer_blur_en_elemento(abl.botonBlur, "hacer_blur_en_elemento_botón_fucos", config.SCREENSHOT_DIR)
    fg.mouse_mueve_y_hace_clic_xy(100, 100, "mouse_mueve_y_hace_clic_x100_y100", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(abl.menExitoso, "El botÃ³n ha perdido el foco y el campo es vÃ¡lido.", "verificar_texto_continido_mensaje_exitoso", config.SCREENSHOT_DIR, 2)
    fg.validar_elemento_no_visible(abl.menError, "validar_elemento_no_visible_mensaje_error", config.SCREENSHOT_DIR)
    
