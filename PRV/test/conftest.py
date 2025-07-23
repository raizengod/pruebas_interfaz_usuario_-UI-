# nombra el archivo: Ve a la ubicación de tu archivo y colcoar el nombre a conftest.py
# La convención de conftest.py le indica a Pytest que este archivo contiene fixtures que deben estar disponibles 
# para los tests en ese directorio y sus subdirectorios.
import pytest
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from datetime import datetime
import os
from typing import Generator
from PRV.utils import config
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_home import HomeLocatorPage
from PRV.locator.locator_barraNavegacion import BarraNavLocatorPage


@pytest.fixture(
    scope="function",
    params=[
        # Resoluciones de escritorio
        {"browser": "chromium", "resolution": {"width": 1920, "height": 1080}, "device": None},
        {"browser": "firefox", "resolution": {"width": 1920, "height": 1080}, "device": None},
        {"browser": "webkit", "resolution": {"width": 1920, "height": 1080}, "device": None},
        # Emulación de dispositivos móviles
        {"browser": "chromium", "device": "iPhone 12", "resolution": None},
        #{"browser": "firefox", "device": "iPhone 12", "resolution": None}, # Descomentar si es necesario
        #{"browser": "webkit", "device": "iPhone 12", "resolution": None},
        {"browser": "webkit", "device": "Pixel 5", "resolution": None}, # Añadido para set_up_AccionBoton y set_up_RadioOption
    ]
)
def playwright_page(playwright: Playwright, request) -> Generator[Page, None, None]:
    """
    Fixture base para configurar el navegador, contexto y página de Playwright con configuraciones comunes.
    Maneja el lanzamiento del navegador, la creación del contexto (con grabación de video y emulación de dispositivos),
    el rastreo (tracing) y la navegación de la página a una URL específica. También renombra el archivo de video al finalizar.
    """
    param = request.param
    browser_type = param["browser"]
    resolution = param["resolution"]
    device_name = param["device"]

    browser_instance = None
    context = None
    page = None

    try:
        if browser_type == "chromium":
            browser_instance = playwright.chromium.launch(headless=True, slow_mo=500)
        elif browser_type == "firefox":
            browser_instance = playwright.firefox.launch(headless=True, slow_mo=500)
        elif browser_type == "webkit":
            browser_instance = playwright.webkit.launch(headless=True, slow_mo=500)
        else:
            raise ValueError(f"\nEl tipo de navegador '{browser_type}' no es compatible.")

        context_options = {
            "record_video_dir": config.VIDEO_DIR,
            "record_video_size": {"width": 1920, "height": 1080}
        }

        if device_name:
            device = playwright.devices[device_name]
            context = browser_instance.new_context(**device, **context_options)
        elif resolution:
            context = browser_instance.new_context(viewport=resolution, **context_options)
        else:
            context = browser_instance.new_context(**context_options)

        page = context.new_page()

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_name_suffix = ""
        if device_name:
            trace_name_suffix = device_name.replace(" ", "_").replace("(", "").replace(")", "")
        elif resolution:
            trace_name_suffix = f"{resolution['width']}x{resolution['height']}"

        trace_file_name = f"traceview_{current_time}_{browser_type}_{trace_name_suffix}.zip"
        trace_path = os.path.join(config.TRACEVIEW_DIR, trace_file_name)

        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page

    finally:
        if context:
            context.tracing.stop(path=trace_path)
            context.close()
            
        if browser_instance:
            browser_instance.close()
            
        if page and page.video:
            video_path = page.video.path()
            new_video_name = datetime.now().strftime("%Y%m%d-%H%M%S") + ".webm"
            new_video_path = os.path.join(config.VIDEO_DIR, new_video_name)
            try:
                os.rename(video_path, new_video_path)
                print(f"\nVideo guardado como: {new_video_path}")
            except Exception as e:
                print(f"\nError al renombrar el video: {e}")

# Reutilizando la fixture base playwright_page
@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que comienzan en BASE_URL.
    """
    playwright_page.goto(config.BASE_URL)
    playwright_page.set_default_timeout(5000)
    yield playwright_page

@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_Formulario_Uno(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que comienzan en FORM_URL e inicializan Funciones_Globales.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    fg = Funciones_Globales(playwright_page)
    fg.esperar_fijo(2)
    yield playwright_page

@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_AccionBoton(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "Acción Botón",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)
    
    fg.esperar_fijo(2)
    
    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None, 2)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioUno, "hacer_click_en_elemento_menú_Formulario_Uno", config.SCREENSHOT_DIR, None)
    fg.hacer_click_en_elemento(bnl.opcionAccionBoton, "hacer_click_en_elemento_link_Practica_menú", config.SCREENSHOT_DIR, None, 1)
    
    fg.validar_url_actual(".*/Botones_ok.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    fg.esperar_fijo(2)
    
    yield playwright_page

@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_RadioOption(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "Opción Radio y Check",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)

    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None, 2)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioUno, "hacer_click_en_elemento_menú_Formulario_Uno", config.SCREENSHOT_DIR, None)
    fg.hacer_click_en_elemento(bnl.opcionCheckboxOption, "hacer_click_en_elemento_link_opcion_CheckBox_Option", config.SCREENSHOT_DIR, None, 1)
    
    fg.validar_url_actual(".*/Radios_Ok.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    fg.esperar_fijo(2)
    
    yield playwright_page
    
@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_Calculadora(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "Calculadora",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)

    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None, 2)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioUno, "hacer_click_en_elemento_menú_Formulario_Uno", config.SCREENSHOT_DIR, None)
    fg.hacer_click_en_elemento(bnl.opcionCalculadora, "hacer_click_en_elemento_link_opcion_calculadora", config.SCREENSHOT_DIR, None, 1)
    
    fg.validar_url_actual(".*/Calculador_ok.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    fg.esperar_fijo(2)
    
    yield playwright_page
    
@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_CamposDos(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "Campos Dos",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)

    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioDos, "hacer_click_en_elemento_menú_Formulario_dos", config.SCREENSHOT_DIR, None, 1)
    fg.hacer_click_en_elemento(bnl.opcionCamposDos, "hacer_click_en_elemento_link_opcion_campos_dos", config.SCREENSHOT_DIR, None, 2)
    
    fg.validar_url_actual(".*/Campos_Dos_OK.htm")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    #fg.esperar_fijo(2)
    
    yield playwright_page
    
@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_ComboBox(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "ComboBox",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)

    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioDos, "hacer_click_en_elemento_menú_Formulario_dos", config.SCREENSHOT_DIR, None, 1)
    fg.hacer_click_en_elemento(bnl.opcionComboBox, "hacer_click_en_elemento_link_opcion_combo_box", config.SCREENSHOT_DIR, None, 2)
    
    fg.validar_url_actual(".*/ComboBox_ok.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    #fg.esperar_fijo(2)
    
    yield playwright_page
    
@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_EsperarCampo(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "ComboBox",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)

    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioDos, "hacer_click_en_elemento_menú_Formulario_dos", config.SCREENSHOT_DIR, None, 1)
    fg.hacer_click_en_elemento(bnl.opcionTiemposEnCampos, "hacer_click_en_elemento_link_opcion_combo_box", config.SCREENSHOT_DIR, None, 2)
    
    fg.validar_url_actual(".*/Tiempos_Ok.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    #fg.esperar_fijo(2)
    
    yield playwright_page
    
@pytest.fixture(scope="function") # Cambiado a 'function' como en tu ejemplo más reciente
def set_up_DragDrop(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "ComboBox",
    incluyendo el manejo del menú móvil.
    """
    playwright_page.goto(config.FORM_URL)
    playwright_page.set_default_timeout(5000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)

    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.hacer_click_en_elemento(bnl.menuHaburguesaFormulario, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None)
        fg.esperar_fijo(1)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    fg.hacer_click_en_elemento(bnl.menuFormularioTres, "hacer_click_en_elemento_menú_Formulario_tres", config.SCREENSHOT_DIR, None, 1)
    fg.hacer_click_en_elemento(bnl.opcionDrapDrop, "hacer_click_en_elemento_link_opcion_drag_and_drop", config.SCREENSHOT_DIR, None, 1)
    
    fg.validar_url_actual(".*/Drag_Drop_ok.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    #fg.esperar_fijo(2)
    
    yield playwright_page