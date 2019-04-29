# coding:utf-8
from requests_html import HTMLSession
import os
import random
import requests
import traceback
import re

def random_ip():
    a = str(random.randint(1, 255))
    b = str(random.randint(1, 255))
    c = str(random.randint(1, 255))
    d = str(random.randint(1, 255))
    ipaddress = '{}.{}.{}.{}'.format(a, b, c, d)
    return ipaddress


def download_mp4(url, mydir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    filename=str(mydir)+'/1.mp4'
    with open(filename,'wb') as f:
        f.write(req.content)
        
        
def download_img(url, mydir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    with open(str(mydir)+'/thumb.png','wb') as f:
        f.write(req.content)


if not os.exists('./fuck91'):
    os.path.mkdir('./fuck91')


flag=2
while flag<=4250:
    tittle=[]
    base_url='http://91porn.com/view_video.php?viewkey='
    page_url='http://91porn.com/v.php?next=watch&page='+str(flag)
    get_page=requests.get(url=page_url)
    viewkey=re.findall(r'<a target=blank href="http://91porn.com/view_video.php\?viewkey=(.*)&page=.*&viewtype=basic&category=.*?">\n                    <img ',str(get_page.content,'utf-8',errors='ignore'))
    
    for key in viewkey:
        headers={'Accept-Language':'zh-CN,zh;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36','X-Forwarded-For':random_ip(),'referer':page_url,'Content-Type': 'multipart/form-data; session_language=cn_CN'}
        video_url=[]
        img_url=[]
        base_req=requests.get(url=base_url+key,headers=headers)
        video_url=re.findall(r'<source src="(.*?)" type=\'video/mp4\'>',str(base_req.content,'utf-8',errors='ignore'))
        tittle=re.findall(r'<div id="viewvideo-title">(.*?)</div>',str(base_req.content,'utf-8',errors='ignore'),re.S)
        img_url=re.findall(r'poster="(.*?)"',str(base_req.content,'utf-8',errors='ignore'))
        
        try:
            t=tittle[0]
            tittle[0]=t.replace('\n','')
            t=tittle[0].replace(' ','')
        except IndexError:
            pass
          
        if os.path.exists(str(t))==False:
            try:
                os.makedirs(str(t))
                print('开始下载:'+str(t))
                download_img(str(img_url[0]), './fuck91/'+str(t))
                download_mp4(str(video_url[0]), './fuck91/'+str(t))
                print('下载完成')
            except:
                pass
        else:
            print('已存在文件夹,跳过')
            
    flag=flag+1
    print('此页已下载完成，下一页是'+str(flag))
