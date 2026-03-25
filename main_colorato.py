from colorama import init, Fore, Back, Style #per stampare colorato
from datetime import date

from gestionale.core.clienti import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.fatture import Fattura
from gestionale.vendite.ordini import RigaOrdine, Ordine

# Inizializza colorama
init(autoreset=True)

# Creare dati
print(Fore.CYAN + Style.BRIGHT + "=== SISTEMA GESTIONALE ===" + Style.RESET_ALL)
print()

cliente = ClienteRecord("Mario Rossi", "mail@mail.com", "Gold")
print(Fore.GREEN + f"✓ Cliente creato: {cliente.nome}")

p1 = ProdottoRecord("Laptop Professional", 1500.0)
p2 = ProdottoRecord("Mouse Wireless", 35.0)
p3 = ProdottoRecord("Tastiera Meccanica", 120.0)

print(Fore.GREEN + f"✓ Prodotti aggiunti: {p1.name}, {p2.name}, {p3.name}")
print()

ordine = Ordine(
    cliente=cliente,
    righe=[
        RigaOrdine(p1, 1),
        RigaOrdine(p2, 2),
        RigaOrdine(p3, 5)
    ]
)

print(Fore.YELLOW + "--- RIEPILOGO ORDINE ---")
print(ordine.riepilogo())
print()

fattura = Fattura(ordine, "2026/100", date.today())

print(Fore.MAGENTA + Style.BRIGHT + "--- FATTURA GENERATA ---")
print(fattura.genera_fattura())

print()
print(Fore.CYAN + "Totale da pagare: " +
      Fore.RED + Style.BRIGHT + f"{ordine.totale_lordo(0.22):.2f}€")