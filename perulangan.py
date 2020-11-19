print ("=======================================")
print ("=                                     =")
print ("=               perulangan            =")
print ("=                                     =")
print ("=======================================")

n = int(input("Masukkan sembarang nilai untuk N :"))
x = 0

while (x < n) :
    if 10**x > n:
        break
    else:
        print("inilah nilai terkecil dari 10^x")
        x = x + 1

print ("jadi, nilai 10^x paling kecil yang lebih dari N adalah :",10**x)
print ("================ selesai ==============")
