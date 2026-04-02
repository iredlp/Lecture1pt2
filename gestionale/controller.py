import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdini()

    def add_ordine(self, e):
        #Prodotto
        nomePstr = self._view._txtInNomeP.value
        try:
            prezzo = float(self._view._txtInPrezzo.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! il prezzo deve essere un numero.",
                        color = "red")
            )
            self._view.update_page()
            return
        try:
            quantita = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! la quantità deve essere un intero.",
                        color="red")
            )
            self._view.update_page()
            return

        #Cliente
        nomeC = self._view._txtInNomeC.value
        mail = self._view._txtInMail.value
        categoria = self._view._txtInCategoria.value

        ordine = self._model.crea_ordine(nomePstr, prezzo,
                                         quantita, nomeC,
                                         mail, categoria)
        self._model.add_ordine(ordine)

        #RIPULISCO L'INTERFCCIA GRAFICA DAI VARI VALORI SALVATI
        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine correttamente inserito.",
                    color="green"))
        self._view._lvOut.controls.append(
            ft.Text("Dettagli dell'ordine:")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo())
        )

        self._view.update_page()



    def gestisci_ordine(self, e):
        pass

    def gestisci_all_ordini(self, e):
        pass

    def stampa_sommario(self, e):
        pass