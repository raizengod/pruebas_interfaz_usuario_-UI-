import random
import pytest
import os # Importa el módulo os para interactuar con el sistema operativo (rutas de archivos, directorios)
from PRV.pages.base_page import Funciones_Globales
from PRV.locator.locator_ComboBox import ComboBoxLocatorPage
from PRV.utils import config # Importa el módulo config para acceder a SCREENSHOT_DIR

def test_verificar_opciones_comboBox(set_up_ComboBox):
    page = set_up_ComboBox # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    cbl = ComboBoxLocatorPage(page)
    
    lista_texto_esperado_uno= ["Seleccione una opción", "Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5"]
    lista_texto_esperado_dos= ["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5"]
    lista_texto_esperado_tres= ["Seleccione un sistema operativo", 
                                "Linux", "Windows", "Mac"]
    
    lista_texto_esperado_cuatro_I=["Seleccione una versión", "Ubuntu", "Fedora", "Debian"]
    lista_texto_esperado_cuatro_II= ["Seleccione una versión", "Windows 7", "Windows 10", "Windows 11"]
    lista_texto_esperado_cuatro_III= ["Seleccione una versión", "macOS Big Sur", "macOS Catalina", "macOS Mojave"]
    
    fg.obtener_y_comparar_valores_dropdown(cbl.comboBoxUno, "obtener_y_comparar_valores_dropdown_uno", config.SCREENSHOT_DIR, lista_texto_esperado_uno)
    fg.obtener_y_comparar_valores_dropdown(cbl.comboBoxDos, "obtener_y_comparar_valores_dropdown_dos", config.SCREENSHOT_DIR, lista_texto_esperado_dos)
    fg.obtener_y_comparar_valores_dropdown(cbl.comboBoxTres, "obtener_y_comparar_valores_dropdown_tres", config.SCREENSHOT_DIR, lista_texto_esperado_tres)
    
    fg.seleccionar_opcion_por_valor(cbl.comboBoxTres, "linux", 'seleccionar_opcion_por_valor_comboBox_tres', config.SCREENSHOT_DIR)
    fg.obtener_y_comparar_valores_dropdown(cbl.comboBoxCuatro, "obtener_y_comparar_valores_dropdown_cuatro", config.SCREENSHOT_DIR, lista_texto_esperado_cuatro_I)
    fg.seleccionar_opcion_por_valor(cbl.comboBoxTres, "windows", 'seleccionar_opcion_por_valor_comboBox_tres', config.SCREENSHOT_DIR)
    fg.obtener_y_comparar_valores_dropdown(cbl.comboBoxCuatro, "obtener_y_comparar_valores_dropdown_cuatro", config.SCREENSHOT_DIR, lista_texto_esperado_cuatro_II)
    fg.seleccionar_opcion_por_valor(cbl.comboBoxTres, "mac", 'seleccionar_opcion_por_valor_comboBox_tres', config.SCREENSHOT_DIR)
    fg.obtener_y_comparar_valores_dropdown(cbl.comboBoxCuatro, "obtener_y_comparar_valores_dropdown_cuatro", config.SCREENSHOT_DIR, lista_texto_esperado_cuatro_III)
    
#@pytest.mark.xfail(reason="Comportamiento atipico de espera aleatoriamente")
def test_seleccionar_por_value(set_up_ComboBox):
    page = set_up_ComboBox # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    cbl = ComboBoxLocatorPage(page)
    
    fg.seleccionar_opcion_por_valor(cbl.comboBoxUno, "5", 'seleccionar_opcion_por_valor_comboBox_uno', config.SCREENSHOT_DIR)
    fg.seleccionar_multiples_opciones_combo(cbl.comboBoxDos, ["1", "3", "4"], 'seleccionar_multiples_opciones_comboBox_dos', config.SCREENSHOT_DIR)
    fg.seleccionar_opcion_por_valor(cbl.comboBoxTres, "windows", 'seleccionar_opcion_por_valor_comboBox_tres', config.SCREENSHOT_DIR)
    fg.seleccionar_opcion_por_valor(cbl.comboBoxCuatro, "Windows 11", 'seleccionar_opcion_por_valor_comboBox_cuatro', config.SCREENSHOT_DIR)
    
    fg.hacer_click_en_elemento(cbl.botonEnviar, "hacer_click_en_elemento_envíar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cbl.menExitoso, "Formulario enviado exitosamente", "verificar_texto_contenido_mensaje_exitoso", config.SCREENSHOT_DIR)
    
def test_seleccionar_por_label(set_up_ComboBox):
    page = set_up_ComboBox # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    cbl = ComboBoxLocatorPage(page)
    
    fg.seleccionar_opcion_por_label(cbl.comboBoxUno, "Valor 2", 'seleccionar_opcion_por_labe_comboBox_uno', config.SCREENSHOT_DIR, "2")
    fg.seleccionar_multiples_opciones_combo(cbl.comboBoxDos, ["2", "4", "5"], 'seleccionar_multiples_opciones_comboBox_dos', config.SCREENSHOT_DIR)
    fg.seleccionar_opcion_por_label(cbl.comboBoxTres, "Mac", 'seleccionar_opcion_por_labe_comboBox_uno', config.SCREENSHOT_DIR, "mac")
    fg.seleccionar_opcion_por_label(cbl.comboBoxCuatro, "macOS Catalina", 'seleccionar_opcion_por_labe_comboBox_uno', config.SCREENSHOT_DIR, None)
    
    fg.hacer_click_en_elemento(cbl.botonEnviar, "hacer_click_en_elemento_envíar", config.SCREENSHOT_DIR)
    fg.verificar_texto_contenido(cbl.menExitoso, "Formulario enviado exitosamente", "verificar_texto_contenido_mensaje_exitoso", config.SCREENSHOT_DIR)
    
def test_seleccion_aleatoria(set_up_ComboBox):
    page = set_up_ComboBox # 'page' es el objeto Page de Playwright

    # IMPORTANTE: Creamos un objeto de tipo función 'Funciones_Globales'
    fg = Funciones_Globales(page)
    # IMPORTANTE: Creamos un objeto de tipo función 'ComboBoxLocatorPage'
    cbl = ComboBoxLocatorPage(page)
    
    # --- ComboBox 1 ---
    # Definición las opciones para ComboBox 1
    opciones_cb1 = ["1", "2", "3", "4", "5"]
    
    # Seleccionar una opción aleatoria directamente de la lista
    # Seleccionar una opción aleatoria directamente de la lista.
    # 'random.choice()' es ideal para elegir UN elemento aleatorio de una secuencia.
    # Es mucho más directo y legible que generar un número y luego mapearlo con 'if/elif'.
    valor_seleccionado_cb1 = random.choice(opciones_cb1)
    fg.seleccionar_opcion_por_valor(cbl.comboBoxUno, valor_seleccionado_cb1, "seleccionar_opcion_por_valor_comboBox_uno", config.SCREENSHOT_DIR)
    
    # --- ComboBox 2 (¡Nueva Optimización!) ---
    # Definir todas las posibles opciones para ComboBox 2
    # Asumimos que los valores internos son '1', '2', '3', '4', '5'
    todas_las_opciones_cb2 = ["1", "2", "3", "4", "5"] 
    
    # 1. Decide aleatoriamente cuántas opciones seleccionar (entre 1 y el total de opciones)
    # Por ejemplo, podemos seleccionar al menos 1 opción, y como máximo todas las disponibles.
    # 'random.randint(a, b)' genera un entero aleatorio N tal que a <= N <= b.
    # Esto permite que la prueba seleccione entre 1 y todas las opciones disponibles, 
    # simulando mejor el uso real.
    cantidad_a_seleccionar = random.randint(1, len(todas_las_opciones_cb2))
    
    # 2. Selecciona aleatoriamente los valores de esa cantidad
    # 'random.sample(population, k)' es perfecto para elegir 'k' elementos ÚNICOS 
    # de una 'population'. Esto evita la selección de la misma opción múltiples veces 
    # en una selección múltiple y es mucho más conciso que cualquier lógica manual.
    valores_multiples_seleccionados = random.sample(todas_las_opciones_cb2, cantidad_a_seleccionar)
    # Ordenar la lista de valores seleccionados
    # Esto es crucial si la aserción de verificación en 'seleccionar_multiples_opciones_combo'
    # espera que los valores recuperados del DOM estén en un orden específico (e.g., ascendente).
    # Asegura que la comparación entre valores esperados y reales sea precisa y sin errores de orden.
    valores_multiples_seleccionados.sort() # Ordena la lista in-place
    
    fg.seleccionar_multiples_opciones_combo(cbl.comboBoxDos, valores_multiples_seleccionados, "seleccionar_multiples_opciones_comboBox_dos", config.SCREENSHOT_DIR)    
        
    # --- ComboBox 3 y ComboBox 4 (Ejemplo de anidamiento más limpio) ---
    # Mapeo de sistemas operativos a sus sub-opciones
    sistemas_operativos = {
        "linux": ["Ubuntu", "Fedora", "Debian"],
        "windows": ["Windows 7", "Windows 10", "Windows 11"],
        "mac": ["macOS Big Sur", "macOS Catalina", "macOS Mojave"]
    }

    # Selecciona un sistema operativo aleatorio directamente de las claves del diccionario.
    # 'random.choice()' es usado nuevamente por su simplicidad para elegir una de las claves.
    so_aleatorio = random.choice(list(sistemas_operativos.keys()))
    fg.seleccionar_opcion_por_valor(cbl.comboBoxTres, so_aleatorio, "seleccionar_opcion_por_valor_comboBox_tres", config.SCREENSHOT_DIR)

    # Selecciona una versión aleatoria del sistema operativo elegido.
    # Accedemos a la lista de versiones usando el SO aleatorio seleccionado, y luego
    # 'random.choice()' elige una versión específica de esa lista.
    versiones_so = sistemas_operativos[so_aleatorio]
    version_aleatoria = random.choice(versiones_so)
    fg.seleccionar_opcion_por_valor(cbl.comboBoxCuatro, version_aleatoria, "seleccionar_opcion_por_valor_comboBox_cuatro", config.SCREENSHOT_DIR)