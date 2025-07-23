from playwright.sync_api import Page

class FormularioUnoLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector de campo Nombre
    @property
    def campoNombre(self):
        return self.page.get_by_role("textbox", name="Nombre:")
    
    #Selector de campo Apellido
    @property
    def campoApellido(self):
        return self.page.get_by_role("textbox", name="Apellidos:")
    
    #Selector de campo Teléfono
    @property
    def campoTelefono(self):
        return self.page.get_by_role("textbox", name="Teléfono:")
    
    #Selector de campo Email
    @property
    def campoEmail(self):
        return self.page.get_by_role("textbox", name="Email:")
    
    #Selector de campo Dirección
    @property
    def campoDirección(self):
        return self.page.get_by_role("textbox", name="Dirección:")
    
    #Selector de botón Eviar
    @property
    def botónEnviar(self):
        return self.page.get_by_role("button", name="Enviar")
    
    #Selector de botón Limpiar
    @property
    def botónLimpiar(self):
        return self.page.get_by_role("button", name="Limpiar")
    
    #Selector mensaje error nombre 
    @property
    def menNombreError(self):
        return self.page.get_by_text("Nombre inválido, no puede")
    
    #Selector mensaje error apellido 
    @property
    def menApellidoError(self):
        return self.page.get_by_text("Apellidos inválidos,, no")
    
    #Selector mensaje error teléfono
    @property
    def menTelefonoError(self):
        return self.page.get_by_text("Teléfono inválido, no Puede")
    
    #Selector mensaje error email 
    @property
    def menEmailError(self):
        return self.page.get_by_text("Email inválido,Formato de")
    
    #Selector mensaje error dirección
    @property
    def menDirecciónError(self):
        return self.page.get_by_text("Dirección inválida,No puede")
    
    #Selector mensaje exitoso
    @property
    def menExitoso(self):
        return self.page.get_by_text("El formulario se ha enviado")