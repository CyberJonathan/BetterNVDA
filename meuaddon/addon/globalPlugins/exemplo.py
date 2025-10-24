import globalPluginHandler #type ignore
import ui #type ignore
import keyboardHandler #type ignore

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):

        super().__init__()
        ui.message("NVDABetter esta ativo")

        def script_digaOElemento(self, gesture):
            focusObject = ui.getFocusObject()
            if focusObject:
                ui.message(f"Elemento focado é: {focusObject.name}")

        def script_LerLinhaAtual(self,gesture):
            
           
            


        
