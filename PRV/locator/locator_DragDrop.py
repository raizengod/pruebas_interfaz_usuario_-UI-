from playwright.sync_api import Page

class DragDropLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector botón refrescar la páfina
    @property
    def botonRefrescarPag(self):
        return self.page.get_by_role("button", name="Refrescar Página")
    
    #Selector objeto drag
    @property
    def objDrag(self):
        return self.page.get_by_text("Arrástrame")
    
    #Selector objeto drag
    @property
    def objDrop(self):
        return self.page.get_by_text("Soltar aquí")
    
    