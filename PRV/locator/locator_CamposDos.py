from playwright.sync_api import Page

class CamposDosLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector campo solo letras
    @property
    def campoSoloLetra(self):
        return self.page.get_by_role("textbox", name="Solo letras")
    
    #Selector campo solo letras y números
    @property
    def campoSoloLetraNum(self):
        return self.page.get_by_role("textbox", name="Letras y números")
    
    #Selector campo email
    @property
    def campoEmail(self):
        return self.page.get_by_role("textbox", name="Correo electrónico")
    
    #Selector campo URL
    @property
    def campoURL(self):
        return self.page.get_by_role("textbox", name="URL")
    
    #Selector campo fecha
    @property
    def campoFecha(self):
        return self.page.get_by_placeholder("Fecha")
    
    #Selector mensaje error solo letra
    @property
    def menErrorSoloLetra(self):
        return self.page.locator("//*[@id='onlyLettersError']")
    
    #Selector mensaje error solo letra y número
    @property
    def menErrorSoloLetraNum(self):
        return self.page.locator("//*[@id='alphanumericError']")
    
    #Selector mensaje error email
    @property
    def menErrorEmail(self):
        return self.page.locator("//*[@id='emailFormatError']")
    
    #Selector mensaje error URL
    @property
    def menErrorURL(self):
        return self.page.locator("//*[@id='urlFormatError']")
    
    #Selector mensaje error fecha
    @property
    def menErrorFecha(self):
        return self.page.locator("//*[@id='dateFormatError']")
    
    #Selector botón enviar
    @property
    def botonEnviar(self):
        return self.page.get_by_role("button", name="Enviar")
    
    #Selector botón limpiar
    @property
    def botonLimpiar(self):
        return self.page.get_by_role("button", name="Limpiar")
    
    #Selector mensaje exitoso
    @property
    def menExitoso(self):
        return self.page.get_by_text("Formulario enviado")