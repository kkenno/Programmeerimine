fmt = "{:50}";
print fmt.format("ARVE 50")
print

fmt = "{:20}{:20}{:20}"

print fmt.format("Arve valjastaja", "Arve Saaja", "Arvenumber: 5647")
print fmt.format("Eesnimi Perenimi", "Eesnimi Perenimi", "Arve kuupaev: 01.01.2011")
print fmt.format("Aadress", "Adress", "Makse tahtaeg: 02.02.2012")
print

fmt = "{:20}{:20}{:20}{:20}"

print fmt.format("Kaup", "Hind", "Kogus", "Kokku")
print fmt.format("Toolid", "5,00", "8", "40,00")
print fmt.format("Lauad", "10,00", "4", "40,00")
print fmt.format("Arvutid", "250,00", "2", "500,00")
print

fmt = "{:60}{:5}"


print fmt.format("Vahesumma", "562,01")
print fmt.format("Kaibemaks 20%", "1420,00")
print fmt.format("Kokku", "98771,00")
print"___________________________________________________________________________"


fmt = "{:20}{:20}"

print fmt.format("Kontaktid", "Arveldus")
print fmt.format("Kaibemaks 20%", "Pank: SEB ")
print fmt.format("Telefon: +372 56471477","Konto: NASN00141510")
