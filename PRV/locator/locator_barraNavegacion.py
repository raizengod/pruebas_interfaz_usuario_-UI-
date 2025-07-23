from playwright.sync_api import Page

class BarraNavLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector menú hamburguesa en formulario
    @property
    def menuHaburguesaFormulario(self):
        return self.page.get_by_role("button", name="Toggle navigation")
        
    """---------- FORMULARIO UNO ----------"""
    
    #Selector desplegable nav formulario uno
    @property
    def menuFormularioUno(self):
        return self.page.get_by_role("button", name="Formularios Validación Uno")
    
    #Selector opción nav formulario uno > campos uno
    @property
    def opcionCamposUnos(self):
        return self.page.get_by_role("link", name="Campos Uno")
    
    #Selector opción nav formulario uno > fomulario
    @property
    def opcionFormulario(self):
        return self.page.get_by_role("link", name="Formulario")
    
    #Selector opción nav formulario uno > acción con botones
    @property
    def opcionAccionBoton(self):
        return self.page.get_by_role("link", name="Acciones Botones")
    
    #Selector opción nav formulario uno > option & chebox
    @property
    def opcionCheckboxOption(self):
        return self.page.get_by_role("link", name="Radio CheckBox")
    
    #Selector opción nav formulario uno > Calculadora
    @property
    def opcionCalculadora(self):
        return self.page.get_by_role("link", name="Calculadora")
    
    """---------- FORMULARIO DOS ----------"""
    
    #Selector desplegable nav formulario dos
    @property
    def menuFormularioDos(self):
        return self.page.get_by_role("button", name="Formularios Validación Dos")
    
    #Selector opción nav formulario dos > campos uno
    @property
    def opcionCamposDos(self):
        return self.page.get_by_role("link", name="Campos Dos")
    
    #Selector opción nav formulario dos > fomulario
    @property
    def opcionComboBox(self):
        return self.page.get_by_role("link", name="ComboBox")
    
    #Selector opción nav formulario dos > acción con botones
    @property
    def opcionVentaProductos(self):
        return self.page.get_by_role("link", name="Venta Productos")
    
    #Selector opción nav formulario dos > option & chebox
    @property
    def opcionLogin(self):
        return self.page.get_by_role("link", name="Login")
    
    #Selector opción nav formulario dos > Calculadora
    @property
    def opcionTiemposEnCampos(self):
        return self.page.get_by_role("link", name="Tiempos en Campos")
    
    """---------- FORMULARIO TRES ----------"""

    #Selector desplegable nav formulario tres
    @property
    def menuFormularioTres(self):
        return self.page.get_by_role("button", name="Formularios Validación tres")
    
    #Selector opción nav formulario tres > drag and drop
    @property
    def opcionDrapDrop(self):
        return self.page.get_by_role("link", name="Drag and Drop")