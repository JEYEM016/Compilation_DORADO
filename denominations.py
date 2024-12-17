name = input("Enter your name :")
amount = eval(input("Input amount deposit:"))


print ("Hi," , name , "Your money deposit breakdown :") 

wankyaw = amount // 1000
wankyaw_ch = amount % 1000

paybh = wankyaw_ch // 500 
paybh_ch = wankyaw_ch % 500

dald = paybh_ch // 200
dald_ch = paybh_ch % 200

wanh = dald_ch // 100 
wanh_ch = dald_ch % 100

pipti = wanh_ch // 50
pipti_ch = wanh_ch % 50

ben = pipti_ch // 20
ben_ch = pipti_ch % 20 

sam = ben_ch // 10
sam_ch = ben_ch % 10

payb = ben_ch // 5
payb_ch = ben_ch // 5

pis = payb_ch // 1 
pis_ch = payb_ch % 1

print (wankyaw , "- Php1000")
print (paybh , "- Php500")
print (dald , "- Php200")
print (wanh , "- Php100")
print (pipti , "- Php50") 
print (ben , "- Php20")
print (sam , "- Php10")
print (payb , "- Php5")
print (pis , "- Php1")


