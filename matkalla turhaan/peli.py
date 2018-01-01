import random

print("Matkalla tur{v,h}aan -simulaattori 2k16\n")
ruutu = 1
vuoro = 0
voitto = 100
vanharuutu = 0
palautukset = 0
odotukset = 0
sattumat = 0
uusiheitto = 0
eteen = 0
arpa = 0
kotipalautukset = 0

yksi = 0
kaksi = 0
kolme = 0
nelja = 0
viisi = 0
kuusi = 0

print("\n[Tarina] Kranaattituli tuhoaa kotisi\n")

while ruutu <= voitto:
  vuoro += 1
  heitto=random.randint(1, 6)
  if heitto == 1:
    yksi += 1
  elif heitto == 2:
    kaksi += 1
  elif heitto == 3:
    kolme += 1
  elif heitto == 4:
    nelja += 1
  elif heitto == 5:
    viisi += 1
  else: kuusi += 1
            
  vanharuutu = ruutu
  ruutu = ruutu + heitto
  print("[Tilastot] Vuoro", vuoro, "olet ruudussa", vanharuutu, "heitit", heitto, "siirryt ruutuun", ruutu)
  
  if ruutu >= voitto:
    print("\n[Lopputulos] Turvapaikkahakemuksesi hyväksyttiin! Pääsit turvaan!\n")
    break
  
  elif ruutu == 3:
    print("\n[Tarina] Isä ja äiti päättävät, että on liian vaarallista jäädä. Lähdet sukulaistesi luo seuraavaan kaupunkiin.\n")
    
  elif ruutu == 7:
    print("\n[Sattumakortti A]\n")
    sattumat +=1
    #tavarat -3
  
  elif ruutu == 9:
    print("\n[Sattumakortti B] Jalkasi ovat rakoilla. Menetät yhden pelivuoron\n")
    sattumat +=1
    vuoro += 1
    odotukset +=1
    
  elif ruutu == 15:
    print("\n[Sattumakortti C] Sotilaat tarkastavat talon, jossa piileskelet. Sinun täytyy antaa heille rahaa. Jos otit mukaasi rahaa, jää paikallesi. Jos et, palaa alkuun.\n")
    sattumat +=1
    palautukset += 1
    ruutu = 1
    
    
  elif ruutu == 19:
    print("\n[Sattumakortti D] Kuulet, että sotilaat etsivät isääsi. Muutat oleskelemaan toiseen taloon. Menetät kaksi pelivuoroa.\n")
    sattumat +=1
    vuoro += 2
    odotukset += 2
    
  elif ruutu == 24:
    print("\n[Sattumakortti E] odota 3\n")
    sattumat +=1
    vuoro += 3
    odotukset += 3
    
  elif ruutu == 26:
    print("\n[Sattumakortti F] ei rahaa, odota 2\n")
    sattumat +=1
    vuoro += 2
    odotukset += 2
    
    
  elif ruutu == 29:
    print("\n[Sattumakortti G] vesi loppuu +2\n")
    sattumat +=1
    vuoro += 2
    odotukset += 2
    
  elif ruutu == 32:
    print("\n[Sattumakortti H]\n")
    sattumat +=1
    vuoro += 1
    odotukset += 1
    
  elif ruutu == 35:
    print("\n[Sattumakortti I]\n")
    sattumat +=1
    vuoro -= 1
    uusiheitto += 1
   
  elif ruutu == 39:
    print("\n[Sattumakortti K]\n")
    sattumat +=1
    palautukset += 1
    ruutu = 13
    
  elif ruutu == 41:
    print("\n[Sattumakortti L]\n")
    sattumat +=1
    vuoro += 2
    odotukset += 2
    
  elif ruutu == 43:
    print("\n[Sattumakortti M]\n")
    sattumat +=1
    vuoro -= 1
    uusiheitto += 1
    
  elif ruutu == 47:
    print("\n[Sattumakortti N]\n")
    sattumat +=1
    ruutu += 6
    eteen += 1
    
  elif ruutu == 53:
    print("\n[Sattumakortti O]\n")
    sattumat +=1
    vuoro += 1
    odotukset += 1
    
  elif ruutu == 58:
    print("\n[Sattumakortti P]\n")
    sattumat +=1
    vuoro += 4
    odotukset += 4
    
  elif ruutu == 64:
    print("\n[Sattumakortti Q]\n")
    sattumat +=1
    vuoro += 3
    odotukset += 3
    
  elif ruutu == 70:
    print("\n[Sattumakortti R] Lentokenttäviranomaiset huomaavat, että viisumisi on väärennetty. He eivät päästä sinua lentokoneeseen.\n[Lopputulos] Jäät paikallesi pelin loppuun asti. Olit matkalla turhaan.\n")
    sattumat +=1
    break
    
  elif ruutu == 76:
    print("\n[Sattumakortti S] Sinut pidätetään saapuessasi maahan. Maahanmuuttoviranomaiset eivät osaa päättää, antavatko sinun jäädä. Kruuna, saat, klaava, takaisin ruutuun 49\n")
    sattumat +=1
    arpa=random.randint(1, 2)
    if arpa == 1:
      palautukset += 1
      ruutu = 49
    
  elif ruutu == 81:
    print("\n[Sattumakortti T]\n")
    sattumat +=1
    vuoro -= 1
    uusiheitto += 1
    
  elif ruutu == 84:
    print("\n[Sattumakortti U]\n")
    sattumat +=1
    ruutu += 6
    eteen += 2
    
  elif ruutu == 87:
    print("\n[Sattumakortti V]\n")
    sattumat +=1
    ruutu += 3
    eteen += 1
    
  elif ruutu == 88:
    print("\n[Sattumakortti W]\n")
    sattumat +=1
    vuoro += 2
    odotukset += 2
    
  elif ruutu == 92:
    print("\n[Sattumakortti X]\n")
    sattumat +=1
    vuoro -= 1
    uusiheitto += 1
    
  elif ruutu == 95:
    print("\n[Sattumakortti Y]\n")
    sattumat +=1
    palautukset += 1
    ruutu -= 3
    vuoro -= 1
    uusiheitto += 1
    
  elif ruutu == 38:
    print("\n[Sattumakortti J] Astuit maamiinaan ja kuolit!\n[Lopputulos] Olit matkalla turhaan.\n")
    sattumat +=1  
    break
    
  elif ruutu == 98:
    print("\n[Sattumakortti Z] Turvapaikkahakemuksesi hylättiin! Sinut palautetaan kotimaahasi!\n")
    kotipalautukset += 1
    sattumat +=1
    ruutu = 1
  
print("Peli ohi! \n")
print("--- Lopulliset tilastot ---\n")
print("Heittovuorojen määrä:", vuoro)
if kotipalautukset >= 1:
  print("Kotimaahan palautuksien määrä:", kotipalautukset)
if palautukset >= 1:
  print("Taaksepäin palautusten määrä:", palautukset)
if eteen >= 1:
  print("Eteenpäin siirtojen määrä:", eteen)
if uusiheitto >= 1:
  print("Uudelleenheittojen määrä:", uusiheitto)
if odotukset >= 1:
  print("Odotettujen vuorojen määrä:", odotukset)
if sattumat >=1:
  print("Sattumakorttien määrä:", sattumat)

print("\nHeittojen jakauma:\n Ykkösiä:", yksi, "\n Kakkosia:", kaksi, "\n Kolmosia", kolme, "\n Nelosia:", nelja, "\n Vitosia:", viisi, "\n Kutosia:", kuusi)