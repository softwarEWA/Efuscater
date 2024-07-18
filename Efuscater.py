_H='# Encrypted by E-Fuscater\n# Github- https://github.com/softwarEWA\n\n'
_G='Dosya ismi  > '
_F='Dosya bulunamadı ?'
_E='Proje ismi > '
_D='Çıktı ismi  > '
_C='cls'
_B='] '
_A='\n['
import os,base64,sys,time
from pprint import pformat
import webbrowser
alfabe=['😀','😃','😄','😁','😅','🤣','😂','😉','😊','😛']
MAX_STR_LEN=70
OFFSET=10
black='\x1b[0;30m'
red='\x1b[0;31m'
green='\x1b[0;32m'
yellow='\x1b[0;33m'
blue='\x1b[0;34m'
purple='\x1b[0;35m'
cyan='\x1b[0;36m'
white='\x1b[0;37m'
soru=green+_A+white+'?'+green+_B+yellow
basarili=green+_A+white+'√'+green+_B
hata=red+_A+white+'!'+red+_B
bilgi=yellow+_A+white+'+'+yellow+_B+cyan
pwd=os.getcwd()
ascıı=f"""
{red}   ███████╗    ██╗    ██╗     █████╗    
{white}   ██╔════╝    ██║    ██║    ██╔══██╗  
{red}   █████╗      ██║ █╗ ██║    ███████║
{white}   ██╔══╝      ██║███╗██║    ██╔══██║
{red}   ███████╗    ╚███╔███╔╝    ██║  ██║
{white}   ╚══════╝     ╚══╝╚══╝     ╚═╝  ╚═╝ 
{cyan}                                   [Geliştirici ~ eware0]
"""
def sprint(sentence,second=.05):
	for A in sentence+'\n':sys.stdout.write(A);sys.stdout.flush();time.sleep(second)
def about():
	os.system(_C);sprint(ascıı,.01);print(f"{cyan}[Tool_İsmi] {purple} :[K-E-fuscater]");print(f"{cyan}[Version]   {purple} :[1.0]");print(f"{cyan}[Author]    {purple} :[eware0]");print(f"{cyan}[Github]    {purple} :[https://github.com/softwarEWA]");print(f"{cyan}[Telegram]  {purple} :[https://t.me/eware0]");print(f"{cyan}[İnstagram] {purple} :[https://instagram.com/eware0]\n");A=input(soru+'menüye gitmek için 1, çıkmak için 0 > '+green)
	if A=='1':main()
	else:exit()
def mover(cıktı_dosyası):
	B=cıktı_dosyası;C=input(soru+'Çıktıyı farklı biryere kayıt etmek istermisin ? (e/h) > '+green)
	if C=='e':
		A=input(soru+'Yolu giriniz > '+green)
		if os.path.exists(A):os.system(f'move "{B}" "{A}"');sprint(f"{basarili}{B} dosyası {A}'ına taşındı\n")
		else:sprint(hata+'Öyle bir yol yok ?!\n')
	else:print('\n')
	exit()
def obfuscate(DEGİSKEN_İ,file_content):
	B=DEGİSKEN_İ;E=base64.b64encode(file_content.encode()).decode();C=0;D=f'{B} = ""\n'
	for H in range(int(len(E)/OFFSET)+1):
		F=''
		for G in E[C:C+OFFSET]:
			A=str(hex(ord(G)))[2:]
			if len(A)<2:A='0'+A
			F+='\\x'+str(A)
		D+=f'{B} += "{F}"\n';C+=OFFSET
	D+=f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({B}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))';return D
def chunk_string(in_s,n):"String'i maksimum n uzunluğunda parçalara ayır";return'\n'.join('{}\\'.format(in_s[A:A+n])for A in range(0,len(in_s),n)).rstrip('\\')
def encode_string(in_s,alfabe):A=dict(enumerate(alfabe));B={B:A for(A,B)in A.items()};return'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n"{}"\n.split("  ")])))\n'.format(pformat(B),chunk_string('  '.join(' '.join(A[int(B)]for B in str(ord(B)))for B in in_s),MAX_STR_LEN))
def obfspyc():
	C='obfuscated.py';B=input(soru+_E+cyan)
	if not os.path.exists(B):sprint(hata+_F);os.system(_C);obfspyc()
	os.system('python o.py '+B+' obfuscated.py');A=input(soru+_D+green)
	with open(C,'r')as D,open(A,'w')as E:F=D.read();E.write('# Encrypted by E-fuscater\n# Github- https://github.com/softwarEWA\n\n'+F)
	os.remove(C);sprint(f"{basarili}{A}'projesi başarı ile {pwd} konumuna kayıt edildi");mover(A);main()
def obfbc():
	A=input(soru+_E+cyan)
	if not os.path.exists(A):sprint(hata+_F);os.system(_C);obfbc()
	os.system('start batch.bat '+A+' obfuscated.bat');sprint(f"{basarili}{A}'projesi başarı ile {pwd} konumuna kayıt edildi");main()
def encryptvar():
	B=input(soru+'Kullanılacak kelimeyi yazınız{red}(GEREKLİ)  > '+green)
	if B=='':sprint(hata+'Kelimeyi yazmadınız');time.sleep(3);encryptvar()
	if B.find(' ')!=-1:sprint(hata+'Sadece 1 kelime girin lütfen');time.sleep(3);encryptvar()
	A=input(soru+'Değişkenin tekrarlanma sayısı  > '+green)
	try:A=int(A)
	except Exception:A=50
	E=B*A;D=input(soru+_G+cyan)
	if not os.path.isfile(D):print(hata+'Dosya bulunamadı');time.sleep(2);encryptvar()
	C=input(soru+_D+green)
	with open(D,'r',encoding='utf-8',errors='ignore')as F,open(C,'w')as G:H=F.read();I=obfuscate(E,H);G.write(_H+I)
	sprint(f"{basarili}{C}'projesi başarı ile {pwd} konumuna kayıt edildi");mover(C)
def encryptem():
	B=input(soru+_G+cyan)
	if not os.path.isfile(B):print(hata+' Dosya bulunamadı');time.sleep(2);encryptem()
	A=input(soru+_D+green)
	with open(B)as D,open(A,'w',encoding='utf-8')as C:C.write(_H);C.write(encode_string(D.read(),alfabe));sprint(f"{basarili}{A}'projesi başarı ile {pwd} konumuna kayıt edildi");mover(A)
def main():
	os.system(_C);sprint(ascıı,.01);print(f"{green}[1]{cyan} Python kodunu{red} karmaşıklaştır (obfuscate)");print(f"{green}[2]{red} Bat kodunu{red} karmaşıklaştır (obfuscate)");print(f"{green}[3]{cyan} Python kodunu bir değişkenle{red} Şifrele");print(f"{green}[4]{yellow} Python kodunu {red}Emojiler ile{cyan} Şifrele");print(f"{green}[5]{yellow} Diğer toollarım");print(f"{green}[6]{yellow} Hakkımda");print(f"{green}[0]{yellow} Çıkış");A=input(f"{soru}{blue}Bir seçim yap : {cyan}")
	while True:
		if A=='1'or A=='01':obfspyc()
		elif A=='2'or A=='02':obfbc()
		elif A=='3'or A=='03':encryptvar()
		elif A=='4'or A=='04':encryptem()
		elif A=='5'or A=='05':
			if os.path.exists('/data/data/com.termux/files/home'):os.system("xdg-open --view 'https://github.com/softwarEWA'")
			else:webbrowser.open('https://github.com/softwarEWA')
			main()
		elif A=='6'or A=='06':about()
		elif A=='0':exit()
		else:sprint(hata+'Yanlış seçim !!');time.sleep(2);main()
if __name__=='__main__':
	try:main()
	except KeyboardInterrupt:sprint(bilgi+'Toolumu kullandığın için teşekkür ederim, kendine cici bak');exit()
	except Exception as e:sprint(hata+str(e))
