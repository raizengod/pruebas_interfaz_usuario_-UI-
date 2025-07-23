from playwright.sync_api import Page

class RadioOptionLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector campo de texto nombre
    @property
    def campoNombre(self):
        return self.page.get_by_placeholder("Nombre")
    
    #Selector campo de texto teléfono
    @property
    def campoTelefono(self):
        return self.page.get_by_placeholder("Telefono")
    
    #Selector mensaje error campo nombre
    @property
    def menErrorNombre(self):
        return self.page.locator("#errorCampo1")
    
    #Selector mensaje error campo nombre
    @property
    def menErrorTelefono(self):
        return self.page.locator("#errorCampo2")
    
    #Selector mensaje error radio option
    @property
    def menErrorOption(self):
        return self.page.get_by_text("Selecciona una opción.")
    
    #Selector mensaje error checkbox
    @property
    def menErrorCheckBox(self):
        return self.page.get_by_text("Selecciona al menos una opció")
    
    #Selector option 1
    @property
    def optionUno(self):
        return self.page.get_by_role("radio", name="Opción 1")
    
    #Selector option 2
    @property
    def optionDos(self):
        return self.page.get_by_role("radio", name="Opción 2")
    
    #Selector checkbox 1
    @property
    def checkBoxUno(self):
        return self.page.get_by_role("checkbox", name="Opción A")
    
    #Selector checkbox 2
    @property
    def checkBoxDos(self):
        return self.page.get_by_role("checkbox", name="Opción B")
    
    #Selector botón enviar
    @property
    def botonEnviar(self):
        return self.page.get_by_role("button", name="Enviar")
    
    #Selector botón limpiar
    @property
    def botonLimpiar(self):
        return self.page.get_by_role("button", name="Limpiar")
    
    #Selector mensaje error general
    @property
    def menErrorGeneral(self):
        return self.page.get_by_text("Por favor, corrige los")
    
    #Selector mensaje exitoso
    @property
    def menExitoso(self):
        return self.page.get_by_text("Formulario enviado")
    
    #Selector mensaje error contador caracteres nombre
    @property
    def menErrorMinCaracterNombre(self):
        return self.page.get_by_text("Debe tener al menos 5")
    
    #Selector mensaje error tipo de dato nombre
    @property
    def menErrorTipoDatoNombre(self):
        return self.page.get_by_text("Debe de ser Texto.")