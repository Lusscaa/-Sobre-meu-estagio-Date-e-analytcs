dados = []
fatu = []
ator = []
with open("actors.csv", "r") as arquivo:
    rob = arquivo.read().replace('"Robert Downey, Jr."','"Robert Downey Jr."').split("\n")
    with open("etapa-5.txt", "w", encoding="utf-8") as arquivo2:
        for linha in rob[1:]:
            ator = (linha.split(",")[0])
            fatu =(linha.split(",")[1])

            arquivo2.write(f"o {ator} tem {fatu}\n")


        
        

        
            



    
    


