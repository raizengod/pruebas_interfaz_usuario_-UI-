import re
import time
import time
import random
from playwright.sync_api import Page, expect, Error , TimeoutError, sync_playwright, Response, Dialog 
from datetime import datetime
import os
from typing import List, Dict, Union, Callable # Asegúrate de que Dict esté aquí
from utils.config import LOGGER_DIR # Importa SCREENSHOT_DIR y LOGGER_DIR de config.py
from utils.logger import setup_logger # Importa setup_logger desde logger.py
import logging # Importa el módulo logging
import openpyxl #Libreria para hacer uso del excel

class Funciones_Globales:
    
    #1- Creamos una función incial 'Constructor'-----ES IMPORTANTE TENER ESTE INICIADOR-----
    def __init__(self, page):
        self.page = page
        self._alerta_detectada = False
        self._alerta_mensaje_capturado = ""
        self._alerta_tipo_capturado = ""
        self._alerta_input_capturado = ""
        self._dialog_handler_registered = False # <--- ¡Esta línea es crucial!

        # --- Nuevas variables para el manejo de pestañas (popups) ---
        self._popup_detectado = False
        self._popup_page = None # Para almacenar el objeto Page de la nueva pestaña
        self._popup_url_capturado = ""
        self._popup_title_capturado = ""  
        
        # Nueva lista para almacenar todas las nuevas páginas abiertas durante una interacción
        self._all_new_pages_opened_by_click: List[Page] = []
        
        # Registramos el manejador de eventos para nuevas páginas
        # Limpiamos la lista al registrar para evitar resagos de pruebas anteriores
        self.page.context.on("page", self._on_new_page)
        # Esto es importante: Si se va a usar _all_new_pages_opened_by_click,
        # necesitamos una forma de reiniciarla o asegurarnos de que solo contenga
        # las páginas relevantes para la acción actual.
        # Una estrategia es limpiar la lista antes de la acción que abre la nueva ventana,
        # y luego recopilar las páginas.
        
        # Configurar el logger para esta clase
        self.logger = setup_logger(name='Funciones_Globales', console_level=logging.INFO, file_level=logging.DEBUG)
        
    #2- Función para generar el nombre de archivo con marca de tiempo
    def _generar_nombre_archivo_con_timestamp(self, prefijo):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3] # Quita los últimos 3 dígitos para milisegundos más precisos
        return f"{timestamp}_{prefijo}"
    
    #3- Función para tomar captura de pantalla
    def tomar_captura(self, nombre_base, directorio):
        """
        Toma una captura de pantalla de la página y la guarda en el directorio especificado.
        Por defecto, usa SCREENSHOT_DIR de config.py.

        Args:
            nombre_base (str): El nombre base para el archivo de la captura de pantalla.
            directorio (str): El directorio donde se guardará la captura. Por defecto, SCREENSHOT_DIR.
        """
        try:
            if not os.path.exists(directorio):
                os.makedirs(directorio)
                self.logger.info(f"\n Directorio creado para capturas de pantalla: {directorio}") #

            nombre_archivo = self._generar_nombre_archivo_con_timestamp(nombre_base) #
            ruta_completa = os.path.join(directorio, f"{nombre_archivo}.png") # Cambiado a .png para mejor calidad
            self.page.screenshot(path=ruta_completa) #
            self.logger.info(f"\n 📸 Captura de pantalla guardada en: {ruta_completa}") #
        except Exception as e:
            self.logger.error(f"\n ❌ Error al tomar captura de pantalla '{nombre_base}': {e}") #
        
    #4- unción basica para tiempo de espera que espera recibir el parametro tiempo
    #En caso de no pasar el tiempo por parametro, el mismo tendra un valor de medio segundo
    def esperar_fijo(self, tiempo=0.5):
        """
        Espera un tiempo fijo en segundos.

        Args:
            tiempo (Union[int, float]): El tiempo en segundos a esperar. Por defecto, 0.5 segundos.
        """
        self.logger.debug(f"\n Esperando fijo por {tiempo} segundos...") #
        try:
            time.sleep(tiempo) #
            self.logger.info(f"Espera fija de {tiempo} segundos completada.") #
        except TypeError:
            self.logger.error(f"\n ❌ Error: El tiempo de espera debe ser un número. Se recibió: {tiempo}") #
        except Exception as e:
            self.logger.error(f"\n ❌ Ocurrió un error inesperado durante la espera fija: {e}") #
        
    #5- Función para indicar el tiempo que se tardará en hacer el scroll
    def scroll_pagina(self, horz, vert, tiempo: Union[int, float] = 0.5):
        """
        Realiza un scroll en la página.

        Args:
            horz (int): Cantidad de scroll horizontal. Por defecto, 0.
            vert (int): Cantidad de scroll vertical. Por defecto, 0.
            tiempo (Union[int, float]): Tiempo de espera después del scroll en segundos. Por defecto, 0.5.
        """
        self.logger.debug(f"Realizando scroll - Horizontal: {horz}, Vertical: {vert}. Espera: {tiempo} segundos.") #
        try:
            self.page.mouse.wheel(horz, vert) #
            self.esperar_fijo(tiempo) # Reutiliza la función esperar_fijo para el log y manejo de errores
            self.logger.info(f"Scroll completado (H: {horz}, V: {vert}).") #
        except Exception as e:
            self.logger.error(f"❌ Error al realizar scroll en la página: {e}") #
            
   
    # --- Manejadores y funciones para Alertas y Confirmaciones ---

    # Handler para alertas simples (usado con page.once)
    def _get_simple_alert_handler_for_on(self):
        def handler(dialog: Dialog):
            self._alerta_detectada = True
            self._alerta_mensaje_capturado = dialog.message
            self._alerta_tipo_capturado = dialog.type
            self.logger.info(f"\n--> [LISTENER ON - Simple Alert] Alerta detectada: Tipo='{dialog.type}', Mensaje='{dialog.message}'") # Se agregó log
            dialog.accept()
            self.logger.info("\n--> [LISTENER ON - Simple Alert] Alerta ACEPTADA.") # Se agregó log
        return handler

    # Handler para diálogos de confirmación (usado con page.once)
    def _get_confirmation_dialog_handler_for_on(self, accion: str):
        def handler(dialog: Dialog):
            self._alerta_detectada = True
            self._alerta_mensaje_capturado = dialog.message
            self._alerta_tipo_capturado = dialog.type
            self.logger.info(f"\n--> [LISTENER ON - Dinámico] Confirmación detectada: Tipo='{dialog.type}', Mensaje='{dialog.message}'") # Se agregó log
            if accion == 'accept':
                dialog.accept()
                self.logger.info("\n--> [LISTENER ON - Dinámico] Confirmación ACEPTADA.") # Se agregó log
            elif accion == 'dismiss':
                dialog.dismiss()
                self.logger.info("--> [LISTENER ON - Dinámico] Confirmación CANCELADA.") # Se agregó log
            else:
                self.logger.warning(f"\n--> [LISTENER ON - Dinámico] Acción desconocida '{accion}'. Aceptando por defecto.") # Se cambió a warning y se agregó log
                dialog.accept()
        return handler    
    
    # Handler para diálogos de pregunta (prompt) (usado con page.once)
    def _get_prompt_dialog_handler_for_on(self, input_text: str, accion: str):
        def handler(dialog: Dialog):
            self._alerta_detectada = True
            self._alerta_mensaje_capturado = dialog.message
            self._alerta_tipo_capturado = dialog.type
            self._alerta_input_capturado = input_text
            self.logger.info(f"\n--> [LISTENER ON - Prompt Dinámico] Diálogo detectado: Tipo='{dialog.type}', Mensaje='{dialog.message}'") # Se agregó log

            if accion == 'accept':
                if dialog.type == "prompt":
                    dialog.accept(input_text)
                    self.logger.info(f"\n--> [LISTENER ON - Prompt Dinámico] Texto '{input_text}' introducido y prompt ACEPTADO.") # Se agregó log
                else:
                    dialog.accept()
                    self.logger.info("\n--> [LISTENER ON - Prompt Dinámico] Diálogo ACEPTADO (sin texto, no es prompt).") # Se agregó log
            elif accion == 'dismiss':
                dialog.dismiss()
                self.logger.info("\n--> [LISTENER ON - Prompt Dinámico] Diálogo CANCELADO.") # Se agregó log
            else:
                self.logger.warning(f"\n--> [LISTENER ON - Prompt Dinámico] Acción desconocida '{accion}'. Cancelando por defecto.") # Se cambió a warning y se agregó log
                dialog.dismiss()
        return handler

    # Handler de eventos para cuando se abre una nueva página.
    def _on_new_page(self, page: Page):
        """
        Manejador de eventos para nuevas páginas (popups).
        """
        self._popup_detectado = True
        self._popup_page = page
        self._popup_url_capturado = page.url
        self._popup_title_capturado = page.title()
        self._all_new_pages_opened_by_click.append(page)
        self.logger.info(f"\n 🌐 Nueva página (popup) detectada. URL: {page.url}")
        # Opcional: Si solo te interesa la primera popup o una específica, podrías manejarlo aquí.
        # Por ahora, solo la añadimos a la lista.
        
    # Handler para hacer drag and drop manual
    def _realizar_drag_and_drop_manual(self, elemento_origen, elemento_destino, nombre_base, directorio, nombre_paso):
        """
        Método privado para realizar Drag and Drop usando las acciones de ratón de bajo nivel.
        Se llama como fallback si el método drag_and_drop() falla.
        """
        try:
            elemento_origen.hover() # Mueve el ratón sobre el elemento de origen
            self.page.mouse.down() # Presiona el botón izquierdo del ratón
            time.sleep(0.5) # Pequeña pausa para simular el arrastre visual
            elemento_destino.hover() # Mueve el ratón sobre el elemento de destino
            time.sleep(0.5) # Pequeña pausa antes de soltar
            self.page.mouse.up() # Suelta el botón izquierdo del ratón
            # No se necesita toma de captura aquí, ya se hizo al inicio del fallback
            # o se hará al final si todo el proceso es exitoso.

        except Error as e:
            error_msg = (
                f"\n ❌ FALLO (Playwright Error - Manual) - {nombre_paso}: Ocurrió un error de Playwright al intentar realizar 'Drag and Drop' manualmente.\n"
                f"Detalles: {e}"
            )
            self.logger.error(error_msg)
            self.tomar_captura(f"{nombre_base}_error_manual_drag_and_drop_playwright", directorio)
            raise
        
        except Exception as e:
            error_msg = (
                f"\n ❌ FALLO (Inesperado - Manual) - {nombre_paso}: Ocurrió un error inesperado al intentar realizar 'Drag and Drop' manualmente.\n"
                f"Detalles: {e}"
            )
            self.logger.error(error_msg)
            self.tomar_captura(f"{nombre_base}_error_inesperado_manual_drag_and_drop", directorio)
            raise