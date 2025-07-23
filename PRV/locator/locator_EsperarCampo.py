from playwright.sync_api import Page

class EsperarCampoLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector label espera
    @property
    def labelEspera(self):
        return self.page.get_by_text("Espera unos segundos")
    
    #Selector campo nombre
    @property
    def campoNombre(self):
        return self.page.get_by_role("textbox", name="Nombre:")
    
    #Selector campo nombre
    @property
    def campoApellido(self):
        return self.page.get_by_role("textbox", name="Apellidos:")
    
    #Selector campo nombre
    @property
    def campoApellido(self):
        return self.page.get_by_role("textbox", name="Apellidos:")
    
    #Selector comboBox
    @property
    def comboBox(self):
        return self.page.get_by_label("ComboBox:")
    
    #Selector comboBox
    @property
    def termCondi(self):
        return self.page.locator("//*[@id='checkbox']")
    
    #Selector botón envíar
    @property
    def botonEnviar(self):
        return self.page.get_by_role("button", name="Enviar")
    
    #Selector botón limpiar
    @property
    def botonLimpiar(self):
        return self.page.get_by_role("button", name="Limpiar")
    
    #Selector botón limpiar
    @property
    def menExitoso(self):
        return self.page.get_by_text("Formulario enviado")
    