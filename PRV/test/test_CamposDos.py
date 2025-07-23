import pytest
import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_CamposDos import CamposDosLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR

#@pytest.mark.xfail(reason="Comportamiento atipico en webkit")    
def test_validar_mensajes_errores_vacios(set_up_CamposDos):
    page = set_up_CamposDos # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'CalculadoraLocatorPage'
    cdl = CamposDosLocatorPage(page)
    
    fg.hacer_click_en_elemento(cdl.botonEnviar, "hacer_click_en_elemento_botón_enviar", config.SCREENSHOT_DIR)
    
    fg.verificar_texto_contenido(cdl.menErrorSoloLetra, "Este campo solo debe contener letras.", "verificar_texto_contenido_solo_letra_vacío", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cdl.menErrorSoloLetraNum, "Este campo solo debe contener letras y números.", "verificar_texto_contenido_solo_letra_y_número_vacío", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cdl.menErrorEmail, "Ingrese un correo electrónico válido.", "verificar_texto_contenido_email_vacío", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cdl.menErrorURL, "Ingrese una URL válida.", "verificar_texto_contenido_URL_vacío", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cdl.menErrorFecha, "Ingrese una fecha válida.", "verificar_texto_contenido_fecha_vacía", config.SCREENSHOT_DIR)

#@pytest.mark.xfail(reason="Comportamiento atipico en webkit")        
def test_completar_formulario_data_xml(set_up_CamposDos):
    page = set_up_CamposDos # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'FormularioUnoLocatorPage'
    cdl = CamposDosLocatorPage(page)
    
    # --- Configuración del archivo XML ---
    # Asume que tienes un archivo XML en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    xml_file_name = "dataset_2.xml"  # Cambia esto al nombre de tu archivo XML
    # 'os.path.join' construye la ruta completa al archivo XML.
    xml_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, xml_file_name)

    # 1. Leer el contenido completo del archivo XML
    try:
        
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
            letra = record_element.find('Solo_letras').text if record_element.find('Solo_letras') is not None else ""
            letraNum = record_element.find('Alfanumérico').text if record_element.find('Alfanumérico') is not None else ""
            correo = record_element.find('Email').text if record_element.find('Email') is not None else ""
            url = record_element.find('URL').text if record_element.find('URL') is not None else ""
            fecha = record_element.find('Fecha').text if record_element.find('Fecha') is not None else ""

            # La fila lógica aquí es solo para propósitos de log y captura
            n_logical_xml_row = i + 1 
            fg.logger.info(f"\nProcesando Fila Lógica XML {n_logical_xml_row}: {letra}, {letraNum}, {correo}, {url}, {url}")

            # Rellenar los campos del formulario
            # Se añade _xml al nombre de la captura para diferenciarla
            fg.rellenar_campo_de_texto(cdl.campoSoloLetra, letra, f"rellenar_solo_letra_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(cdl.campoSoloLetraNum, letraNum, f"rellenar_solo_letra_número_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(cdl.campoEmail, correo, f"rellenar_email_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(cdl.campoURL, url, f"rellenar_url_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.rellenar_campo_de_texto(cdl.campoFecha, fecha, f"rellenar_fecha_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)

            fg.logger.info(f"\nDatos de fila XML {n_logical_xml_row} cargados: {letra} {letraNum} {correo} {url} {url}")

            fg.hacer_click_en_elemento(cdl.botonEnviar, f"enviar_formulario_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR, "Enviar", 1)
            fg.verificar_texto_contenido(cdl.menExitoso, "Formulario enviado exitosamente", f"confirmacion_envio_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR)
            fg.hacer_click_en_elemento(cdl.botonLimpiar, f"limpiar_formulario_fila_{n_logical_xml_row}_xml", config.SCREENSHOT_DIR, "Limpiar", 1)

    except Exception as e:
        fg.logger.error(f"\n ❌ Ocurrió un error inesperado durante el procesamiento del XML: {e}")
        raise # Re-lanza la excepción para que Pytest marque la prueba como fallida
    
#@pytest.mark.xfail(reason="Comportamiento atipico en webkit")
def test_completar_formulario_data_excel(set_up_CamposDos):
    page = set_up_CamposDos # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'FormularioUnoLocatorPage'
    cdl = CamposDosLocatorPage(page)
    
    # --- Configuración del archivo Excel ---
    # Asume que tienes un archivo Excel en la ruta SOURCE_FILES_DIR_DATA_FUENTE
    # Por ejemplo: "datos_formulario.xlsx"
    excel_file_name = "MOCK_DATA_2.xlsx"  # Cambia esto al nombre de tu archivo Excel
    # 'os.path.join' construye la ruta completa al archivo Excel.
    # 'config.SOURCE_FILES_DIR_DATA_FUENTE' es una variable (definida en 'config.py')
    # que apunta al directorio donde se espera que estén tus archivos de datos fuente.
    excel_file_path = os.path.join(config.SOURCE_FILES_DIR_DATA_FUENTE, excel_file_name)
    sheet_name = "data"  # Nombre de la hoja dentro del archivo Excel desde la cual se leerán los datos.
    has_header = True # Indica si la primera fila de la hoja de Excel contiene encabezados (nombres de columna) o si los datos empiezan desde la primera fila.

    # 1. Obtener el número de filas del Excel
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
        letras = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Solo letras") #
        letrasNum = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Letras y Números") #
        correo = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Email") #
        url = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "URL") #
        fecha = fg.dato_Columna_excel(excel_file_path, sheet_name, n, "Fecha") #

        fg.logger.info(f"\nProcesando Fila {n}: {letras}, {letrasNum}, {correo}, {url}, {fecha}") # Usa el logger

        # Rellenar los campos del formulario usando los localizadores de FormularioUnoLocatorPage
        # y las funciones de Funciones_Globales
        fg.rellenar_campo_de_texto(cdl.campoSoloLetra, letras, f"rellenar_letras_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(cdl.campoSoloLetraNum, letrasNum, f"rellenar_letras_número_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(cdl.campoEmail, correo, f"rellenar_correo_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(cdl.campoURL, url, f"rellenar_URL_fila_{n}", config.SCREENSHOT_DIR) #
        fg.rellenar_campo_de_texto(cdl.campoFecha, fecha, f"rellenar_fecha_fila_{n}", config.SCREENSHOT_DIR) #

        fg.logger.info(f"Datos de fila {n} cargados: {letras} {letrasNum} {correo} {url} {fecha}") # Usa el logger

        fg.hacer_click_en_elemento(cdl.botonEnviar, f"enviar_formulario_fila_{n}", config.SCREENSHOT_DIR, "Enviar", 1) #
        # Asumiendo que 'Men_Confir' se refiere a 'verificar_mensaje_confirmacion_o_error' o similar de tu base_page
        # Si no tienes un método exacto 'Men_Confir', necesitas adaptarlo a tu función de validación de mensajes.
        # Aquí se usa verificar_texto_contenido para un mensaje genérico.
        fg.verificar_texto_contenido(cdl.menExitoso, "Formulario enviado exitosamente", f"confirmacion_envio_fila_{n}", config.SCREENSHOT_DIR) #
        fg.hacer_click_en_elemento(cdl.botonLimpiar, f"limpiar_formulario_fila_{n}", config.SCREENSHOT_DIR, "Limpiar", 1) #