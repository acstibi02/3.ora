nem = input("Add meg a nemed:(fiú:m/lány:f)")

if nem == "f":
    kor = int(input("Hány éves vagy?: "))
    if kor >= 10 and kor <= 12:
        print("Gratulálok, játszhatsz a csapatban. ")
    else:
        print("Sajnálom, nem téged keresünk!")
else:
    print("Sajnálom, nem téged keresünk!")