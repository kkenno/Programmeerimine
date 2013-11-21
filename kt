#KT1

tekst = raw_input("sisesta tekst: ")
print tekst.upper()
print tekst.lower()
print "", tekst.center(80," ")
print tekst.replace(" ","_")

#KT2

print tekst.upper(), len(tekst), tekst.lower()

#KT3

print "see tekst on pikem kui 10 m2rki: "+str(len(tekst)>10)

if " " not in tekst:
        print "tekstis puudub tyhik"
else:
        print "tekstis on tyhik"

if "x" not in tekst:
        print "tekstis puudub x"
else:
        print "tekstis on x"
if tekst == "":
        print "teksti pole"
else:
        print "tekst on olemas"

if tekst.isdigit():
        print "sisaldab numbrit"
else:
        print "ei sisalda numbrit"

if tekst == tekst.upper():
        print "tekstis on suuri t2hti"
else: 
        print "tekstis pole suuri t2hti"

#KT4

print
this = "{:<30} {:20} {:>30}"
length = len(tekst)
hash_tag = "#" * length
print this.format(tekst.upper(), "|"+hash_tag+ "|", tekst.lower())


#KT5

sum(x in ".!" for x in tekst)



