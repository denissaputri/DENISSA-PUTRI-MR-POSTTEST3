print ("                                               ")
print ("============== pembelian takoyaki =============")
print ("                                               ")
print ("                                               ")
jenis_varian = input("varian 1 atau varian 2 : ")
varian1 = 'varian 1'
varian2 = 'varian 2'

if(jenis_varian == 'varian 1'):
    pembelian_var1 = int(input('== pembelian varian 1 (porsi): '))
    harga_var1 = 2000 
    total_var1 = int(pembelian_var1) * harga_var1
    if (pembelian_var1) >= 10 : 
         diskon = total_var1* 10/100 
         harga_bayar1 = total_var1 - diskon
         print('"pembelian varian 1 sebanyak 10 porsi/lebih diskon 10% "')
            print("harga total pembelian         : Rp ",total_var1)
            print("Potongan Harga                : Rp ",diskon)
            print("jadi harga yang harus dibayar : Rp %s" % harga_bayar1) 
        
    else:
          diskon = 0
          print('"Maaf pembelian varian 1 kurang dari 10 porsi dikenakan harga normal"')
          print("harga varian 1/pcs            : Rp ", harga_var1)
          print("total                         : Rp ",total_var1)
          print("harga yang harus dibayar      : Rp ",total_var1)
        
elif(jenis_varian == 'varian 2'):
    pembelian_var2 = int(input('== pembelian varian 2(porsi): '))
    harga_var2 = 2500
    total_var2 = int(pembelian_var2) * harga_var2
    if (pembelian_var2) >= 8 : 
           diskon = total_var2 * 8/100 
           harga_bayar2 = total_var2 - diskon
           print('"pembelian varian 2 sebanyak 8 porsi/lebih diskon 8% "')
           print("harga total pembelian         : Rp ",total_var2)
           print("Potongan Harga                : Rp ",diskon)
           print("jadi harga yang harus dibayar : Rp %s" % harga_bayar2) 
    else: 
            diskon = 0 
            print('"Maaf pembelian varian 1 kurang dari 10 porsi dikenakan harga normal"')
            print("harga varian 2/pcs            : Rp ",harga_var2)
            print("total                         : Rp ",total_var2)
            print("harga yang harus dibayar      : Rp ",total_var2)
else: 
    print('"maaf varian takoyaki tidak dapat dicampur"')
print('')
print('=================terima kasih =======================')
