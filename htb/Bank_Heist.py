from itertools import product
import string
dictionnare={'2':'A', '22':'B', '222':'C',
'3' : 'D', '33' : 'E', '333' : 'F',
'4' : 'G', '44' : 'H', '444' : 'I',
'5' : 'J', '55' : 'K', '555' : 'L',
'6' : 'M', '66' : 'N', '666' : 'O',
'7' : 'P', '77' : 'Q', '777' : 'R', '7777' : 'S',
'8' : 'T', '88' : 'U', '888' : 'V',
'9' : 'W', '99' : 'X', '999' : 'Y', '9999' : 'Z',
}
cipher_text='''29337777666 633'''
cipher_text=cipher_text.split()
def get_word(number):
    word=number[0]
    plain=""
    for i in range(1,len(number)):
        if number[i]==number[i-1]:
            word+=number[i]
        else:
            plain+=dictionnare[word]
            word=number[i]
    plain+=dictionnare[word]
    return plain
plain_text=""
for ele in cipher_text:
    plain_text+=get_word(ele)
    plain_text+=' '
print(plain_text)
# IF YOU AEE EEADING THE CIPHEE YOU AEE OKAY YOUE SHAEE OF THE HEIST IS IN YOUE HOUSE THE KEY TO THE LOCK IS BELOW GO TO PAEIS 
# GSV XLWV GL GSV HZU OLXP TLIVGEIVNVMGUFMW
#FLAG: HTB{GORETIREMENTFUND!!}