from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_home import HomeLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR

def test_ir_a_opcion_practica(set_up):
    page = set_up # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'HomeLocatorPage'
    hl = HomeLocatorPage(page)

    # --- Lógica para manejar el menú hamburguesa en dispositivos móviles ---
    # Puedes definir un umbral de ancho para considerar un dispositivo móvil
    # Por ejemplo, si el ancho del viewport es menor o igual a 768 píxeles.
    ancho_viewport = page.viewport_size['width']

    if ancho_viewport <= 768:
        # Haz clic en el menú hamburguesa
        # Asegúrate de que este localizador sea el correcto para tu menú hamburguesa.
        fg.hacer_click_en_elemento(hl.menuHamburguesa, "clic_menu_hamburguesa", config.SCREENSHOT_DIR, None, 2)
        fg.esperar_fijo(1) # Pequeña espera para que el menú se despliegue
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")

    # El resto de tu lógica de prueba continúa normalmente
    # El enlace 'Prácticas2' podría estar visible directamente o después de abrir el menú hamburguesa.
    fg.hacer_click_en_elemento(hl.linkPracticaMenu, "hacer_click_en_elemento_link_Practica_menú", config.SCREENSHOT_DIR, None, 3)
    
    fg.validar_url_actual("https://validaciones.rodrigovillanueva.com.mx/index.html")
    fg.validar_titulo_de_web("Formulario de Ejemplo", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    fg.esperar_fijo(2)