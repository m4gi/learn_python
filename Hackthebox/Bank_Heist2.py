import string

lower=list(string.ascii_lowercase)
vocabularie="GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW"
flag=vocabularie.split()
FLAG=""
for ele in flag:
    for char in ele:
        number=25-lower.index(char.lower())
        FLAG+=lower[number].upper()
    FLAG+=" "
print(FLAG)