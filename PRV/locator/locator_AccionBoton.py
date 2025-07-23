from playwright.sync_api import Page

class AccionBotonLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector campo de texto nombre
    @property
    def campoNombre(self):
        return self.page.locator("#nombre")
    
    #Selector mensaje error
    @property
    def menError(self):
        return self.page.get_by_text("El campo no puede estar vacÃo.")
    
    #Selector mensaje exitoso
    @property
    def menExitoso(self):
        return self.page.locator("#flashMessage")
    
    #Selector botón click
    @property
    def botonClick(self):
        return self.page.get_by_role("button", name="Click Me", exact=True)
    
    #Selector botón doble click
    @property
    def botonDobleClick(self):
        return self.page.get_by_role("button", name="Doble Click Me")
    
    #Selector botón hover over
    @property
    def botonHoverOver(self):
        return self.page.get_by_role("button", name="Hover Over Me")
    
    #Selector botón right click
    @property
    def botonRightClick(self):
        return self.page.get_by_role("button", name="Right Click Me")
    
    #Selector botón mouse down
    @property
    def botonMouseDown(self):
        return self.page.get_by_role("button", name="Mouse Down")
    
    #Selector botón mouse up
    @property
    def botonMouseUp(self):
        return self.page.get_by_role("button", name="Mouse Up")
    
    #Selector botón focus
    @property
    def botonFocus(self):
        return self.page.get_by_role("button", name="Focus Me")
    
    #Selector botón blur
    @property
    def botonBlur(self):
        return self.page.get_by_role("button", name="Blur Me")
    
    
    