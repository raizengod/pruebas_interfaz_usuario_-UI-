from playwright.sync_api import Page

class HomeLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector de link de practica
    @property
    def menuHamburguesa(self):
        return self.page.locator("//*[@id='menu-bar']")
    
    #Selector de link de practica
    @property
    def linkPracticaMenu(self):
        return self.page.locator("#block-notech-subtheme-main-menu > div > div > ul").get_by_role("link", name="Prácticas2")