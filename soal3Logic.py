def hitungVokal(str) :
    counter=0
    vocal = set('aiueoAIUEO')
    for i in str:
        if i in vocal:
            counter += 1
    print('Jumlah Vokal :',counter)

# hitungVokal("Indonesia")
a  = input("Masukan Kata : ")
hitungVokal(a)