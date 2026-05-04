
import flet as ft

from gestionale.controller import Controller
from UI.view import View


def main(page: ft.Page):
    v = View(page) #così ho passato come argomento la pagina e in questo modo sa dove scriverci le cose
    c = Controller(v)
    v.set_controller(c)
    v.carica_interfaccia()#creo tutti gli ggtti grafici, inizializzarli al controller e fare gli elementi grafici
#CONTROLLER E VIEW SI PARLANO

ft.app(target = main)
