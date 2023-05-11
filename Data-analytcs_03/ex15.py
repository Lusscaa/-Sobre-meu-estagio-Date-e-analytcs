class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada


l = Lampada(False)
l.liga()
print("A lâmpada está ligada?", l.esta_ligada())
l.desliga()
print("A lâmpada ainda está ligada?", l.esta_ligada())
