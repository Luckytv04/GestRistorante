class Prenotazione:
    
    prenotazione = []
    
    def __init__(self, nome_cliente, numero_persone, data, ora):
        self.nome_cliente = nome_cliente
        self.numero_persone = numero_persone
        self.data = data
        self.ora = ora
        
    def aggiungi_prenotazione(self):
        self.prenotazione.append(self)
        
    def __str__(self):
        return f"{self.nome_cliente} ha prenotato per {self.numero_persone} persone il giorno {self.data} alle ore {self.ora}"
    
    def visualizza_prenotazioni(self):
        for prenotazione in self.prenotazione:
            print(prenotazione)
    
    

scelta = int(input("1. Aggiungi prenotazione\n2. Visualizza prenotazioni\n3. Elimina prenotazione\n4. Modifica prenotazione\n5. Esci\n \n"))

match scelta:
    case 1:
        aggiungi_prenotazione = Prenotazione(input("Nome: "), int(input("Num. persone: ")), input("Per la data: "), input("All'ora: "))
        print(aggiungi_prenotazione)
    
    case 2:
        Prenotazione.visualizza_prenotazioni(input("Immettere la data di prenotazione: "))