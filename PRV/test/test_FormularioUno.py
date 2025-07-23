import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_FormularioUno import FormularioUnoLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR

def test_validar_visibilidad_formulario_uno(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    fg.validar_elemento_visible(ful.campoNombre, "validar_campo_nombre_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ful.campoApellido, "validar_campo_apellido_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ful.campoTelefono, "validar_campo_teléfono_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ful.campoEmail, "validar_campo_email_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ful.campoDirección, "validar_campo_dirección_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ful.botónEnviar, "validar_botón_enviar_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_visible(ful.botónLimpiar, "validar_botón_limpiar_Visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ful.menNombreError, "validar_mensaje_error_nombre_no_visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ful.menApellidoError, "validar_mensaje_error_apellido_no_visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ful.menTelefonoError, "validar_mensaje_error_teléfono_no_visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ful.menEmailError, "validar_mensaje_error_email_no_visible", config.SCREENSHOT_DIR)
    fg.validar_elemento_no_visible(ful.menDirecciónError, "validar_mensaje_error_dirección_no_visible", config.SCREENSHOT_DIR)
    
def test_campos_vacios(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    fg.hacer_click_en_elemento(ful.botónEnviar, "hacer_click_con_campos_vacíos", config.SCREENSHOT_DIR, "Enviar", 1)
    
    fg.verificar_texto_contenido(ful.menNombreError, "Nombre inválido, no puede estar vacio,mayor que 3 y tiene que ser Texto", "verificar_texto__mensaje_nombre_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menApellidoError, "Apellidos inválidos,, no puede estar vacio,mayor que 3 y tiene que ser Texto", "verificar_texto__mensaje_apellido_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menTelefonoError, "Teléfono inválido, no Puede estar vacio y tiene que ser un numero,tienen que ser 10 numeros", "verificar_texto__mensaje_teléfono_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menEmailError, "Email inválido,Formato de email invalido", "verificar_texto__mensaje_email_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menDirecciónError, "Dirección inválida,No puede estar vacio, Minimo 10 caracteres máximo 30", "verificar_texto__mensaje_dirección_error_visible", config.SCREENSHOT_DIR)
    
def test_data_incorrecta(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    page.reload()
    
    fg.rellenar_campo_de_texto(ful.campoNombre, "N", "rellenar_nombre_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoApellido, "A", "rellenar_epallido_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoTelefono, "T", "rellenar_teléfono_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoEmail, "e@e.c", "rellenar_email_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoDirección, "D", "rellenar_dirección_data_incorrecta", config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(ful.botónEnviar, "hacer_click_data_incorrecta", config.SCREENSHOT_DIR, "Enviar", 1)
    
    fg.verificar_texto_contenido(ful.menNombreError, "Nombre inválido, no puede estar vacio,mayor que 3 y tiene que ser Texto", "verificar_texto__mensaje_nombre_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menApellidoError, "Apellidos inválidos,, no puede estar vacio,mayor que 3 y tiene que ser Texto", "verificar_texto__mensaje_apellido_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menTelefonoError, "Teléfono inválido, no Puede estar vacio y tiene que ser un numero,tienen que ser 10 numeros", "verificar_texto__mensaje_teléfono_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menEmailError, "Email inválido,Formato de email invalido", "verificar_mensaje_email_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menDirecciónError, "Dirección inválida,No puede estar vacio, Minimo 10 caracteres máximo 30", "verificar_texto__mensaje_dirección_error_visible", config.SCREENSHOT_DIR)
    
def test_limpiar_datos_formulario(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    fg.hacer_click_en_elemento(ful.botónLimpiar, "hacer_click_botón_limpiar", config.SCREENSHOT_DIR, "Limpiar")
    
    fg.verificar_valor_campo(ful.campoNombre, "", "verificar_campo_nombre_vacío", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(ful.campoApellido, "", "verificar_campo_apellido_vacío", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(ful.campoTelefono, "", "verificar_campo_teléfono_vacío", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(ful.campoEmail, "", "verificar_campo_email_vacio", config.SCREENSHOT_DIR)
    fg.verificar_valor_campo(ful.campoDirección, "", "verificar_campo_dirección_vacio", config.SCREENSHOT_DIR)
    
def test_caracteres_minimos(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    fg.rellenar_campo_de_texto(ful.campoNombre, "ABC", "rellenar_nombre_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoApellido, "DEF", "rellenar_epallido_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(ful.campoTelefono, 1234567890, "rellenar_teléfono_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoEmail, "g@h.ij", "rellenar_email_data_incorrecta", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoDirección, "KLMNÑOPQRS", "rellenar_dirección_data_incorrecta", config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(ful.botónEnviar, "hacer_click_data_incorrecta", config.SCREENSHOT_DIR, "Enviar", 1)
    
    fg.verificar_texto_contenido(ful.menExitoso, "El formulario se ha enviado correctamente.", "verificar_texto_mensaje_exitoso_visible", config.SCREENSHOT_DIR)
    
def test_caracteres_mayor_a_maximo(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    texto= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis lobortis neque. Sed id aliquet massa. Integer quis lectus in sapien mollis malesuada sed eu mi. Nulla urna turpis, fringilla vitae fermentum vel, imperdiet at urna. In vel consequat ligula. Fusce porttitor neque id nulla pellentesque auctor. Aenean iaculis ex."
    numero= 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
    email= "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890@1234123456789012345678901234567890123456789012345678901234567890.acdefgh"
    
    fg.rellenar_campo_de_texto(ful.campoNombre, texto, "caracteres_nombre_mayor_máximo", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoApellido, texto, "caracteres_apellido_mayor_máximo", config.SCREENSHOT_DIR)
    fg.rellenar_campo_numerico_positivo(ful.campoTelefono, numero, "caracteres_teléfono_mayor_máximo", config.SCREENSHOT_DIR)
    #fg.rellenar_campo_de_texto(ful.campoEmail, email, "caracteres_email_mayor_máximo", config.SCREENSHOT_DIR)
    fg.rellenar_campo_de_texto(ful.campoDirección, texto, "caracteres_dirección_mayor_máximo", config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(ful.botónEnviar, "hacer_click_data_incorrecta", config.SCREENSHOT_DIR, "Enviar", 1)
    
    fg.verificar_texto_contenido(ful.menNombreError, "Nombre inválido, no puede estar vacio,mayor que 3 y tiene que ser Texto", "verificar_texto__mensaje_nombre_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menApellidoError, "Apellidos inválidos,, no puede estar vacio,mayor que 3 y tiene que ser Texto", "verificar_texto__mensaje_apellido_error_visible", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(ful.menTelefonoError, "Teléfono inválido, no Puede estar vacio y tiene que ser un numero,tienen que ser 10 numeros", "verificar_texto__mensaje_teléfono_error_visible", config.SCREENSHOT_DIR)
    
    fg.verificar_texto_contenido(ful.menDirecciónError, "Dirección inválida,No puede estar vacio, Minimo 10 caracteres máximo 30", "verificar_texto__mensaje_dirección_error_visible", config.SCREENSHOT_DIR)
    
def test_completar_formulario_data_excel(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    # --- Configuración del archivo Excel ---
    # Asume que tienes un archivo Excel en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    # Por ejemplo: "datos_formulario.xlsx"
    excel_file_name = "MOCK_DATA.xlsx"  # Cambia esto al nombre de tu archivo Excel
    # 'os.path.join' construye la ruta completa al archivo Excel.
    # 'config.SOURCE_FILES_DIR_DATA_FUENTE' es una variable (definida en 'config.py')
    # que apunta al directorio donde se espera que estén tus archivos de datos fuente.
    excel_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, excel_file_name)
    sheet_name = "data"  # Nombre de la hoja dentro del archivo Excel desde la cual se leerán los datos.
    has_header = True # Indica si la primera fila de la hoja de Excel contiene encabezados (nombres de columna) o si los datos empiezan desde la primera fila.

    # 1. Obtener el número de filas del Excel
    fg.hacer_click_en_elemento(ful.botónLimpiar, "hacer_click_botón_limpiar", config.SCREENSHOT_DIR, "Limpiar")
    # Obtener el número de filas del Excel utilizando la función de Funciones_Globales
    num_filas = fg.num_Filas_excel(excel_file_path, sheet_name, has_header) #

    # Determinar el índice de inicio de las filas de datos.
    # Si tiene encabezado, los datos útiles empiezan desde la fila 2 (índice 2 para openpyxl).
    # Si no tiene encabezado, empiezan desde la fila 1 (índice 1 para openpyxl).
    start_row_index = 2 if has_header else 1

    # Iterar sobre las filas de datos
    # El rango debe ser desde 'start_row_index' hasta 'num_filas + start_row_index'
    # para incluir todas las filas de datos.
    for n in range(start_row_index, num_filas + start_row_index):
        # Obtener datos de cada columna por su nombre (más robusto que el índice numérico)
        # Asegúrate que los nombres de las columnas coincidan con los de tu Excel.
        nombre = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Nombre") #
        apellido = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Apellido") #
        telef = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Telefono") #
        correo = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Email") #
        direccion = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Direccion") #

        fg.logger.info(f"\nProcesando Fila {n}: {nombre}, {apellido}, {telef}, {correo}, {direccion}") # Usa el logger

        # Rellenar los campos del formulario usando los localizadores de FormularioUnoLocatorPage
        # y las funciones de Funciones_Globales
        fg.rellenar_campo_de_texto(ful.campoNombre, nombre, f"rellenar_nombre_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(ful.campoApellido, apellido, f"rellenar_apellido_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(ful.campoTelefono, telef, f"rellenar_telefono_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(ful.campoEmail, correo, f"rellenar_correo_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(ful.campoDirección, direccion, f"rellenar_direccion_fila_{n}", config.SCREENSHOT_DIR) #

        fg.logger.info(f"Datos de fila {n} cargados: {nombre} {apellido} {telef} {correo} {direccion}") # Usa el logger

        fg.hacer_click_en_elemento(ful.botónEnviar, f"enviar_formulario_fila_{n}", config.SCREENSHOT_DIR, "Enviar", 1) #
        # Asumiendo que 'Men_Confir' se refiere a 'verificar_mensaje_confirmacion_o_error' o similar de tu base_page
        # Si no tienes un método exacto 'Men_Confir', necesitas adaptarlo a tu función de validación de mensajes.
        # Aquí se usa verificar_texto_contenido para un mensaje genérico.
        fg.verificar_texto_contenido(ful.menExitoso, "El formulario se ha enviado correctamente.", f"confirmacion_envio_fila_{n}", config.SCREENSHOT_DIR) #
        fg.hacer_click_en_elemento(ful.botónLimpiar, f"limpiar_formulario_fila_{n}", config.SCREENSHOT_DIR, "Limpiar", 1) #

def test_completar_formulario_data_csv(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'FormularioUnoLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    # --- Configuración del archivo CSV ---
    # Asume que tienes un archivo CSV en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    csv_file_name = "MOCK_DATA.csv"  # Cambia esto al nombre de tu archivo CSV
    # 'os.path.join' construye la ruta completa al archivo CSV.
    csv_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, csv_file_name)
    delimiter_csv = "," # Define el delimitador de tu archivo CSV (ej. ',', ';', '\t')
    has_header_csv = True # Indica si la primera fila del CSV contiene encabezados.

    # 1. Obtener el número de filas de datos del CSV
    
    fg.hacer_click_en_elemento(ful.botónLimpiar, "hacer_click_botón_limpiar_csv", config.SCREENSHOT_DIR, "Limpiar")
    # Obtener el número de filas de DATOS útiles del CSV utilizando la función de Funciones_Globales
    num_data_rows_csv = fg.num_Filas_csv(csv_file_path, delimiter_csv, has_header_csv) 

    # Iterar sobre las filas de datos
    # 'n_logical_data_row' representará el índice lógico de la fila de datos (1-based).
    # Esto es consistente con cómo dato_Columna_csv espera la 'fila'.
    for n_logical_data_row in range(1, num_data_rows_csv + 1):
        # Obtener datos de cada columna por su ÍNDICE numérico.
        # Asegúrate que los índices de las columnas coincidan con los de tu CSV.
        # Ejemplo: Columna 1 (Nombre), Columna 2 (Apellido), etc.
        # Si tu CSV tiene el mismo orden que tu Excel, los índices serán:
        # Nombre = 1, Apellido = 2, Telefono = 3, Email = 4, Direccion = 5
        nombre = fg.dato_Columna_csv(csv_file_path, n_logical_data_row, 1, delimiter_csv, has_header_csv) # Columna 1 para Nombre
        apellido = fg.dato_Columna_csv(csv_file_path, n_logical_data_row, 2, delimiter_csv, has_header_csv) # Columna 2 para Apellido
        telef = fg.dato_Columna_csv(csv_file_path, n_logical_data_row, 3, delimiter_csv, has_header_csv) # Columna 3 para Telefono
        correo = fg.dato_Columna_csv(csv_file_path, n_logical_data_row, 4, delimiter_csv, has_header_csv) # Columna 4 para Email
        direccion = fg.dato_Columna_csv(csv_file_path, n_logical_data_row, 5, delimiter_csv, has_header_csv) # Columna 5 para Direccion

        fg.logger.info(f"\nProcesando Fila Lógica CSV {n_logical_data_row}: {nombre}, {apellido}, {telef}, {correo}, {direccion}")

        # Rellenar los campos del formulario
        # Se añade _csv al nombre de la captura para diferenciarla
        fg.rellenar_campo_de_texto(ful.campoNombre, nombre, f"rellenar_nombre_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR)
        fg.rellenar_campo_de_texto(ful.campoApellido, apellido, f"rellenar_apellido_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR)
        fg.rellenar_campo_de_texto(ful.campoTelefono, telef, f"rellenar_telefono_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR)
        fg.rellenar_campo_de_texto(ful.campoEmail, correo, f"rellenar_correo_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR)
        fg.rellenar_campo_de_texto(ful.campoDirección, direccion, f"rellenar_direccion_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR)

        fg.logger.info(f"Datos de fila CSV {n_logical_data_row} cargados: {nombre} {apellido} {telef} {correo} {direccion}")

        fg.hacer_click_en_elemento(ful.botónEnviar, f"enviar_formulario_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR, "Enviar", 1)
        fg.verificar_texto_contenido(ful.menExitoso, "El formulario se ha enviado correctamente.", f"confirmacion_envio_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR)
        fg.hacer_click_en_elemento(ful.botónLimpiar, f"limpiar_formulario_fila_{n_logical_data_row}_csv", config.SCREENSHOT_DIR, "Limpiar", 1)

def test_completar_formulario_data_json(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'FormularioUnoLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    # --- Configuración del archivo JSON ---
    # Asume que tienes un archivo JSON en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    json_file_name = "MOCK_DATA.json"  # Cambia esto al nombre de tu archivo JSON
    # 'os.path.join' construye la ruta completa al archivo JSON.
    json_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, json_file_name)

    # 1. Leer el contenido completo del archivo JSON
    try:
        fg.hacer_click_en_elemento(ful.botónLimpiar, "hacer_click_botón_limpiar_json", config.SCREENSHOT_DIR, "Limpiar")
        
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
            apellido = record.get("apellido")
            telef = record.get("telefono")
            correo = record.get("email")
            direccion = record.get("direccion")

            # La fila lógica aquí es solo para propósitos de log y captura, indicando qué registro se procesa.
            # Empieza desde 1 para ser más amigable.
            n_logical_json_row = i + 1 
            fg.logger.info(f"\nProcesando Fila Lógica JSON {n_logical_json_row}: {nombre}, {apellido}, {telef}, {correo}, {direccion}")

            # Rellenar los campos del formulario
            # Se añade _json al nombre de la captura para diferenciarla
            fg.rellenar_campo_de_texto(ful.campoNombre, nombre, f"rellenar_nombre_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoApellido, apellido, f"rellenar_apellido_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoTelefono, telef, f"rellenar_telefono_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoEmail, correo, f"rellenar_correo_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoDirección, direccion, f"rellenar_direccion_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)

            fg.logger.info(f"\nDatos de fila JSON {n_logical_json_row} cargados: {nombre} {apellido} {telef} {correo} {direccion}")

            fg.hacer_click_en_elemento(ful.botónEnviar, f"enviar_formulario_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR, "Enviar", 1)
            fg.verificar_texto_contenido(ful.menExitoso, "El formulario se ha enviado correctamente.", f"confirmacion_envio_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR)
            fg.hacer_click_en_elemento(ful.botónLimpiar, f"limpiar_formulario_fila_{n_logical_json_row}_json", config.SCREENSHOT_DIR, "Limpiar", 1)

    except Exception as e:
        fg.logger.error(f"\n ❌ Ocurrió un error inesperado durante el procesamiento del JSON: {e}")
        raise # Re-lanza la excepción para que Pytest marque la prueba como fallida

def test_completar_formulario_data_xml(set_up_Formulario_Uno):
    page = set_up_Formulario_Uno # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'FormularioUnoLocatorPage'
    ful = FormularioUnoLocatorPage(page)
    
    # --- Configuración del archivo XML ---
    # Asume que tienes un archivo XML en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    xml_file_name = "dataset.xml"  # Cambia esto al nombre de tu archivo XML
    # 'os.path.join' construye la ruta completa al archivo XML.
    xml_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, xml_file_name)

    # 1. Leer el contenido completo del archivo XML
    try:
        fg.hacer_click_en_elemento(ful.botónLimpiar, "hacer_click_botón_limpiar_xml", config.SCREENSHOT_DIR, "Limpiar")
        
        # Leer el XML. Se espera que devuelva el elemento raíz.
        root_element = fg.leer_xml(xml_file_path)

        # Verificar que el elemento raíz se leyó correctamente
        if root_element is None:
            fg.logger.error("\n ❌ Error: No se pudo leer el archivo XML o está vacío/mal formado.")
            # Dependiendo de tu lógica de negocio, podrías lanzar una excepción o simplemente retornar.
            raise ValueError("No se pudo procesar el archivo XML.")

        # Iterar sobre los elementos 'record' dentro del XML
        # Asegúrate de que 'record' sea el tag correcto para cada entrada de datos
        records = root_element.findall('record') 

        if not records:
            fg.logger.warning(f"\n ⚠️ Advertencia: El archivo XML '{xml_file_path}' no contiene elementos '<record>' o está vacío.")
            return # Termina la prueba si no hay datos para procesar

        # Iterar sobre cada elemento 'record'
        for i, record_element in enumerate(records):
            # Obtener datos de cada campo buscando por el nombre del tag
            # Se usa .find('TagName') y luego .text para obtener el contenido
            # Se añade una verificación para None. Si el elemento no existe, .text lanzaría un error.
            nombre = record_element.find('nombre').text if record_element.find('nombre') is not None else ""
            apellido = record_element.find('apellido').text if record_element.find('apellido') is not None else ""
            telef = record_element.find('telefono').text if record_element.find('telefono') is not None else ""
            correo = record_element.find('email').text if record_element.find('email') is not None else ""
            direccion = record_element.find('direccion').text if record_element.find('direccion') is not None else ""

            # La fila lógica aquí es solo para propósitos de log y captura
            n_logical_xml_row = i + 1 
            fg.logger.info(f"\nProcesando Fila Lógica XML {n_logical_xml_row}: {nombre}, {apellido}, {telef}, {correo}, {direccion}")

            # Rellenar los campos del formulario
            # Se añade _xml al nombre de la captura para diferenciarla
            fg.rellenar_campo_de_texto(ful.campoNombre, nombre, f"rellenar_nombre_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoApellido, apellido, f"rellenar_apellido_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoTelefono, telef, f"rellenar_telefono_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoEmail, correo, f"rellenar_correo_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(ful.campoDirección, direccion, f"rellenar_direccion_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)

            fg.logger.info(f"\nDatos de fila XML {n_logical_xml_row} cargados: {nombre} {apellido} {telef} {correo} {direccion}")

            fg.hacer_click_en_elemento(ful.botónEnviar, f"enviar_formulario_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR, "Enviar", 1)
            fg.verificar_texto_contenido(ful.menExitoso, "El formulario se ha enviado correctamente.", f"confirmacion_envio_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.hacer_click_en_elemento(ful.botónLimpiar, f"limpiar_formulario_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR, "Limpiar", 1)

    except Exception as e:
        fg.logger.error(f"\n ❌ Ocurrió un error inesperado durante el procesamiento del XML: {e}")
        raise # Re-lanza la excepción para que Pytest marque la prueba como fallida
