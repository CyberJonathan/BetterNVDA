import globalPluginHandler 
import ui
import keyboardHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):

        super().__init__()
        ui.message("NVDABetter esta ativo")

        def script_digaOElemento(self, gesture):
            focusObject = ui.getFocusObject()
            if focusObject:
                ui.message(f"Elemento focado é: {focusObject.name}")
            else:
                ui.message("Nenhum elemento focado.")
