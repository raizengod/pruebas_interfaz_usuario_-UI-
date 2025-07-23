from playwright.sync_api import Page

class ComboBoxLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector comboBox 1
    @property
    def comboBoxUno(self):
        return self.page.get_by_label("ComboBox 1:")
    
    #Selector comboBox 2
    @property
    def comboBoxDos(self):
        return self.page.get_by_label("ComboBox 2 (Multi-selección):")
    
    #Selector comboBox 3
    @property
    def comboBoxTres(self):
        return self.page.get_by_label("Sistema Operativo:")
    
    #Selector comboBox 3
    @property
    def comboBoxCuatro(self):
        return self.page.get_by_label("Versión:")
    
    #Selector botón envíar
    @property
    def botonEnviar(self):
        return self.page.get_by_role("button", name="Enviar")
    
    #Selector botón envíar
    @property
    def botonLimpiar(self):
        return self.page.get_by_role("button", name="Limpiar")
    
    #Selector mensaje exitoso
    @property
    def menExitoso(self):
        return self.page.get_by_text("enviado")
