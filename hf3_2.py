regi_ar = int(input("Add meg a termék eredeti árát: "))

if regi_ar < 10000:
    print(regi_ar*0.9,"a kedvezményes ár és",regi_ar/10,"a kedvezmény.")
else:
    print(regi_ar*0.8, "a kedvezményes ár és", (regi_ar / 100)*20, "a kedvezmény.")