import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_barraNavegacion import BarraNavLocatorPage
from PRV.locator.locator_RadioOption import RadioOptionLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR
    
def test_validar_mensajes_errores(set_up_RadioOption):
    page = set_up_RadioOption # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'RadioOptionLocatorPage'
    rol = RadioOptionLocatorPage(page)
    
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.hacer_blur_en_elemento(rol.botonEnviar, "hacer_blur_en_elemento_botón_enviar", config.SCREENSHOT_DIR)
    
    fg.verificar_texto_contenido(rol.menErrorNombre, "Este campo es obligatorio.", "verificar_texto_contenido_mensaje_error_nombre", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorTelefono, "Este campo es obligatorio.", "verificar_texto_contenido_mensaje_error_teléfono", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorOption, "Selecciona una opción.", "verificar_texto_contenido_mensaje_error_option", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorCheckBox, "Selecciona al menos una opción.", "verificar_texto_contenido_mensaje_error_checkBox", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorGeneral, "Por favor, corrige los errores en el formulario.", "verificar_texto_contenido_mensaje_error_general", config.SCREENSHOT_DIR)
    
def test_data_incorrecta_nombre(set_up_RadioOption):
    page = set_up_RadioOption # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'RadioOptionLocatorPage'
    rol = RadioOptionLocatorPage(page)
    
    fg.rellenar_campo_de_texto(rol.campoNombre, "Nombre", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.validar_elemento_no_visible(rol.menErrorNombre, "validar_elemento_no_visible_mensaje_error_nombre", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorTelefono, "Este campo es obligatorio.", "verificar_texto_contenido_mensaje_error_teléfono", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorOption, "Selecciona una opción.", "verificar_texto_contenido_mensaje_error_option", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorCheckBox, "Selecciona al menos una opción.", "verificar_texto_contenido_mensaje_error_checkBox", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorGeneral, "Por favor, corrige los errores en el formulario.", "verificar_texto_contenido_mensaje_error_general", config.SCREENSHOT_DIR)
    
    fg.rellenar_campo_numerico_positivo(rol.campoTelefono, 1234567890, "rellenar_campo_de_texto_teléfono", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.validar_elemento_no_visible(rol.menErrorNombre, "validar_elemento_no_visible_mensaje_error_nombre", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorTelefono, "validar_elemento_no_visible_mensaje_error_teléfono", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorOption, "Selecciona una opción.", "verificar_texto_contenido_mensaje_error_option", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorCheckBox, "Selecciona al menos una opción.", "verificar_texto_contenido_mensaje_error_checkBox", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorGeneral, "Por favor, corrige los errores en el formulario.", "verificar_texto_contenido_mensaje_error_general", config.SCREENSHOT_DIR)
    
    fg.marcar_checkbox(rol.optionDos, "marcar_option", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.validar_elemento_no_visible(rol.menErrorNombre, "validar_elemento_no_visible_mensaje_error_nombre", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorTelefono, "validar_elemento_no_visible_mensaje_error_teléfono", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorOption, "validar_elemento_no_visible_mensaje_error_option", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorCheckBox, "Selecciona al menos una opción.", "verificar_texto_contenido_mensaje_error_checkBox", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menErrorGeneral, "Por favor, corrige los errores en el formulario.", "verificar_texto_contenido_mensaje_error_general", config.SCREENSHOT_DIR)
    
    fg.marcar_checkbox(rol.checkBoxUno, "marcar_checkbox", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.validar_elemento_no_visible(rol.menErrorNombre, "validar_elemento_no_visible_mensaje_error_nombre", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorTelefono, "validar_elemento_no_visible_mensaje_error_teléfono", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorOption, "validar_elemento_no_visible_mensaje_error_option", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorCheckBox, "validar_elemento_no_visible_mensaje_error_checkBox", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(rol.menErrorGeneral, "validar_elemento_no_visible_mensaje_error_general", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(rol.menExitoso, "Formulario enviado correctamente.", "verificar_texto_contenido_mensaje_exitoso", config.SCREENSHOT_DIR)
    
def test_limpiar_datos(set_up_RadioOption):
    page = set_up_RadioOption # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'RadioOptionLocatorPage'
    rol = RadioOptionLocatorPage(page)
    
    fg.hacer_click_en_elemento(rol.botonLimpiar, "hacer_click_en_elemento_botón_limpiar", config.SCREENSHOT_DIR, "Limpiar")
    fg.verificar_valor_campo(rol.campoNombre, "", "verificar_valor_campo_nombre_vacio", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(rol.campoTelefono, "", "verificar_valor_campo_teléfono_vacio", config.SCREENSHOT_DIR)
    fg.verificar_estado_checkbox_o_select(rol.optionUno, False, "vverificar_estado_optionuno", config.SCREENSHOT_DIR)
    fg.verificar_estado_checkbox_o_select(rol.optionDos, False, "verificar_estado_option_dos", config.SCREENSHOT_DIR)
    fg.verificar_estado_checkbox_o_select(rol.checkBoxUno, False, "verificar_estado_checkbox_uno", config.SCREENSHOT_DIR)
    fg.verificar_estado_checkbox_o_select(rol.checkBoxDos, False, "verificar_valor_checkbox_dos", config.SCREENSHOT_DIR)

def test_completar_campos_individual(set_up_RadioOption):
    page = set_up_RadioOption # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'RadioOptionLocatorPage'
    rol = RadioOptionLocatorPage(page)
    
    fg.rellenar_campo_de_texto(rol.campoNombre, "123", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.verificar_texto_contenido(rol.menErrorMinCaracterNombre, "Debe tener al menos 5 caracteres.", "verificar_texto_contenido_mensaje_error_minimo_caracteres_nombre", config.SCREENSHOT_DIR)
    
    fg.rellenar_campo_de_texto(rol.campoNombre, "12345", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.verificar_texto_contenido(rol.menErrorTipoDatoNombre, "Debe de ser Texto.", "verificar_texto_contenido_mensaje_error_tipo_dato_nombre", config.SCREENSHOT_DIR)
    
    fg.rellenar_campo_de_texto(rol.campoNombre, "Nombre Dos", "rellenar_campo_de_texto_nombre", config.SCREENSHOT_DIR)
    fg.hacer_click_en_elemento(rol.botonEnviar, "hacer_click_en_elemento_enviar", config.SCREENSHOT_DIR, "Enviar")
    fg.validar_elemento_no_visible(rol.menErrorNombre, "validar_elemento_no_visible_mensaje_error_nombre", config.SCREENSHOT_DIR)
    
def test_rellenar_form_data_json(set_up_RadioOption):
    page = set_up_RadioOption # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'RadioOptionLocatorPage'
    rol = RadioOptionLocatorPage(page)
    
    # --- Configuración del archivo JSON ---
    # Asume que tienes un archivo JSON en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    json_file_name = "MOCK_DATA_2.json"  # Cambia esto al nombre de tu archivo JSON
    # 'os.path.join' construye la ruta completa al archivo JSON.
    json_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, json_file_name)

    # 1. Leer el contenido completo del archivo JSON
    try:
        fg.hacer_click_en_elemento(rol.botonLimpiar, "hacer_click_botón_limpiar_json", config.SCREENSHOT_DIR, "Limpiar")
        
        # Leer el JSON. Se espera que devuelva una lista de diccionarios (registros).
        data_from_json = fg.leer_json(json_file_path)

        # Verificar que los datos JSON se leyeron correctamente y son una lista
        if not isinstance(data_from_json, list):
            fg.logger.error(f"\n ❌ Error: El contenido del JSON no es una lista de registros como se esperaba. Tipo: {type(data_from_json)}")
            raise ValueError("El archivo JSON debe contener una lista de registros.")
        if not data_from_json:
            fg.logger.warning(f"\n ⚠️ Advertencia: El archivo JSON '{json_file_path}' está vacío o no contiene registros.")
            return # Termina la prueba si no hay datos para procesar

        # Iterar sobre cada diccionario (registro) en la lista de datos del JSON
        for i, record in enumerate(data_from_json):
            # Obtener datos de cada campo usando las claves del diccionario
            # Asegúrate que las claves ('Nombre', 'Apellido', etc.) coincidan con las de tu JSON.
            # Se usa .get() para evitar errores si una clave no existe, devolviendo None por defecto.
            nombre = record.get("nombre")
            telef = record.get("telefono")
            optUno = record.get("option 1")
            optDos = record.get("option 2")
            chkUno = record.get("check a")
            chkDos = record.get("check b")

            # La fila lógica aquí es solo para propósitos de log y captura, indicando qué registro se procesa.
            # Empieza desde 1 para ser más amigable.
            n_logical_json_row = i + 1 
            fg.logger.info(f"\nProcesando Fila Lógica JSON {n_logical_json_row}: {nombre}, {telef}, {optUno}, {optDos}, {chkUno}, {chkDos}")

            # Rellenar los campos del formulario
            # Se añade _json al nombre de la captura para diferenciarla
            fg.rellenar_campo_de_texto(rol.campoNombre, nombre, f"rellenar_nombre_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(rol.campoTelefono, telef, f"rellenar_telefono_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            if (optUno == True):
                fg.marcar_checkbox(rol.optionUno, f"marcar_option_uno_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            if (optDos == True):
                fg.marcar_checkbox(rol.optionDos, f"marcar_option_dos_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            if (chkUno == True):
                fg.marcar_checkbox(rol.checkBoxUno, f"marcar_checkBox_uno_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            if (chkDos == True):
                fg.marcar_checkbox(rol.checkBoxDos, f"marcar_checkBox_dos_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)

            fg.logger.info(f"\nDatos de fila JSON {n_logical_json_row} cargados: {nombre} {telef} {optUno} {optDos} {chkUno} {chkDos}")

            fg.hacer_click_en_elemento(rol.botonEnviar, f"enviar_formulario_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR, "Enviar", 1)
            fg.verificar_texto_contenido(rol.menExitoso, "Formulario enviado correctamente.", f"confirmacion_envio_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.hacer_click_en_elemento(rol.botonLimpiar, f"limpiar_formulario_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR, "Limpiar", 1)

    except Exception as e:
        fg.logger.error(f"\n ❌ Ocurrió un error inesperado durante el procesamiento del JSON: {e}")
        raise # Re-lanza la excepción para que Pytest marque la prueba como fallida
    
    