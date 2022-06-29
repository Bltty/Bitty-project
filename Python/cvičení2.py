b = ("-----------------------")
k = ("kalkulačka urokové sazby na  spoření")
j = ("-----------------------")


kolik_vlozi = int(input("zadejte kolik chcete vložit: "))
uroková_sazba  = float(input("kolik procent máte urokovou sazbu: "))
kolik_let_spořit = int(input("kolik  let chcete spořit: "))
idk = 100

výpočet_procent = uroková_sazba/idk*kolik_vlozi
print("za rok dostanete")
print (výpočet_procent)
print("------------------------")

celkove = výpočet_procent * kolik_let_spořit
print("za vámi zvolený časové období se vám naspoří: ")
print(celkove)
print("-----------------------------------------------")

print("celkově  na  učte  za vámu zvolení čas budete mít: ")
na_ucte = kolik_vlozi + celkove
print(na_ucte)
print("-------------------------------------------------------")

inflace = float(input("zadejte velikost inflace:"))
inflaci = inflace / idk * na_ucte
vypocet_inflace = inflaci - na_ucte
print("-------------------------------------------------")
print("znehodnotilo se vám: ")
print(vypocet_inflace)
print("----------------------------------------")
print("děkujeme  za využitý naší kalkulačky")
