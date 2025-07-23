import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_Calculadora import CalculadoraLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR
    
def test_validar_mensajes_errores_vacios(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    fg.hacer_click_en_elemento(cl.botonMultiplicar, "hacer_click_en_elemento_botón_multiplicar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoUno, "Este campo es obligatorio.", "verificar_texto_contenido_mensaje_error_campo_uno_vacío", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, 2, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.menErrorCampoUno, "validar_elemento_no_visible_error_campo_uno", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoDos, "Este campo es obligatorio.", "verificar_texto_contenido_mensaje_error_campo_dos_vacío", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, 4, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.menErrorCampoDos, "validar_elemento_no_visible_error_campo_dos", config.SCREENSHOT_DIR)
    
def test_validar_mensajes_errores_tipo_dato(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    fg.rellenar_campo_de_texto(cl.campoNumeroUno, "abc", "rellenar_campo_de_texto_uno_alfabético", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoUno, "Debe ser un número válido.", "verificar_texto_contenido_mensaje_error_campo_uno_tipo_dato", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoNumeroUno, "123,56", "rellenar_campo_de_texto_uno_con_coma", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoUno, "Debe ser un número válido.", "verificar_texto_contenido_mensaje_error_campo_uno_tipo_dato", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, 15.25, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.menErrorCampoUno, "validar_elemento_no_visible_error_campo_uno", config.SCREENSHOT_DIR)
    
    fg.rellenar_campo_de_texto(cl.campoNumeroDos, "def", "rellenar_campo_de_texto_uno_alfabético", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonMultiplicar, "hacer_click_en_elemento_botón_multiplicar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoDos, "Debe ser un número válido.", "verificar_texto_contenido_mensaje_error_campo_dos_tipo_dato", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoNumeroDos, "789,01", "rellenar_campo_de_texto_uno_con_coma", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoDos, "Debe ser un número válido.", "verificar_texto_contenido_mensaje_error_campo_dos_tipo_dato", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, 20.02, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.menErrorCampoDos, "validar_elemento_no_visible_error_campo_dos", config.SCREENSHOT_DIR)
    
def test_validar_mensajes_errores_numero_negativo(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    fg.rellenar_campo_de_texto(cl.campoNumeroUno, "-152.23", "rellenar_campo_de_texto_uno_alfabético", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoUno, "Debe ser un número positivo.", "verificar_texto_contenido_mensaje_error_campo_uno_tipo_dato", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, 152.23, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.menErrorCampoUno, "validar_elemento_no_visible_error_campo_uno", config.SCREENSHOT_DIR)
    
    fg.rellenar_campo_de_texto(cl.campoNumeroDos, "-20.02", "rellenar_campo_de_texto_uno_alfabético", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonMultiplicar, "hacer_click_en_elemento_botón_multiplicar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cl.menErrorCampoDos, "Debe ser un número positivo.", "verificar_texto_contenido_mensaje_error_campo_dos_tipo_dato", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, 20.02, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.menErrorCampoDos, "validar_elemento_no_visible_error_campo_dos", config.SCREENSHOT_DIR)
    
def test_boton_limpiar(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    valor1= 123.56
    valor2= 15.25
    resultadoFloat= valor1 - valor2
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor1, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor2, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(cl.campoNumeroUno, "", "verificar_valor_campo_uno_vacío", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(cl.campoNumeroDos, "", "verificar_valor_campo_dos_vacío", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(cl.campoResultado, "", "verificar_valor_campo_resultado_vacío", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(cl.campoResultadoCopiar, "validar_elemento_no_visible_campo_resultado_copia", config.SCREENSHOT_DIR)
    
def test_hacer_suma(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    valor1= 123.56
    valor2= 15.25
    resultadoFloat= valor1 + valor2
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor1, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor2, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    
    valor3= 1023
    valor4= 235
    resultadoInt= valor3 + valor4
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor3, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor4, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_int(cl.campoResultado, resultadoInt, "verificar_valor_campo_numerico_int_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_int(cl.campoResultadoCopiar, resultadoInt, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    
    valor5= 235
    valor6= 102323.123
    resultadoFloat2= valor5 + valor6
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor5, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor6, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonSumar, "hacer_click_en_elemento_botón_sumar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat2, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat2, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    
def test_hacer_resta(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    valor1= 123.56
    valor2= 15.25
    resultadoFloat= valor1 - valor2
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor1, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor2, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    
    valor3= 1023
    valor4= 235
    resultadoInt= valor3 - valor4
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor3, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor4, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_int(cl.campoResultado, resultadoInt, "verificar_valor_campo_numerico_int_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_int(cl.campoResultadoCopiar, resultadoInt, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    
    valor5= 235
    valor6= 102323.123
    resultadoFloat2= valor5 - valor6
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor5, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor6, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonRestar, "hacer_click_en_elemento_botón_restar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat2, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat2, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    
def test_hacer_multiplicar(set_up_Calculadora):
    page = set_up_Calculadora # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cl = CalculadoraLocatorPage(page)
    
    valor1= 123.56
    valor2= 15.25
    resultadoFloat= valor1 * valor2
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor1, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor2, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonMultiplicar, "hacer_click_en_elemento_botón_multiplicar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    
    valor3= 1023
    valor4= 0
    resultadoInt= valor3 * valor4
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor3, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor4, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonMultiplicar, "hacer_click_en_elemento_botón_multiplicar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_int(cl.campoResultado, resultadoInt, "verificar_valor_campo_numerico_int_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_int(cl.campoResultadoCopiar, resultadoInt, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonLimpiar,"hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR)
    
    valor5= 0
    valor6= 102323.123
    resultadoFloat2= valor5 * valor6
    
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroUno, valor5, "rellenar_campo_numérico_positivo_uno", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(cl.campoNumeroDos, valor6, "rellenar_campo_numérico_positivo_dos", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(cl.botonMultiplicar, "hacer_click_en_elemento_botón_multiplicar", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultado, resultadoFloat2, "verificar_valor_campo_numerico_float_resultado", config.SCREENSHOT_DIR)
    copiar= fg.obtener_valor_elemento_enable(cl.campoResultado, "obtener_valor_elemento_enable_resultado", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(cl.campoResultadoCopiar, copiar, "rellenar_campo_de_texto_copia_resultado", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo_numerico_float(cl.campoResultadoCopiar, resultadoFloat2, "verificar_valor_campo_copia_resultado", config.SCREENSHOT_DIR)