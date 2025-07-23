from playwright.sync_api import Page

class CalculadoraLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector campo numérico uno
    @property
    def campoNumeroUno(self):
        return self.page.get_by_role("textbox", name="Número 1")
    
    #Selector campo numérico dos
    @property
    def campoNumeroDos(self):
        return self.page.get_by_role("textbox", name="Número 2")
    
    #Selector campo numérico resultado
    @property
    def campoResultado(self):
        return self.page.locator("#resultado")
    #Selector campo numérico resultado
    @property
    def campoResultadoCopiar(self):
        return self.page.locator("#resultado2")
    
    #Selector botón sumar
    @property
    def botonSumar(self):
        return self.page.get_by_role("button", name="Sumar")
    
    #Selector botón restar
    @property
    def botonRestar(self):
        return self.page.get_by_role("button", name="Restar")
    
    #Selector botón multiplicar
    @property
    def botonMultiplicar(self):
        return self.page.get_by_role("button", name="Multiplicar")
    
    #Selector botón dividir
    @property
    def botonLimpiar(self):
        return self.page.get_by_role("button", name="Limpiar")
    
    #Selector mensaje error número uno vacío
    @property
    def menErrorCampoUno(self):
        return self.page.locator("//*[@id='errorNumero1']")
    
    #Selector mensaje error número dos vacío
    @property
    def menErrorCampoDos(self):
        return self.page.locator("#errorNumero2")