# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

cookie = 'Hm_lvt_46d556462595ed05e05f009cdafff31a=1666432616; htVC_2132_saltkey=vlee2xew; htVC_2132_lastvisit=1675207549; htVC_2132_client_created=1675240283; htVC_2132_client_token=C93F1A76EC47ECD2A272EB96A7651B4A; htVC_2132_auth=a4fflFYRa1tPt3KNM0sXjbOfUX2oMbPDTPzbwlWWZI%2B1ol27tc3qn3MBTISKh2sWJLM2wfj%2FVEizPqtVMzVsI7nC6rHq; htVC_2132_connect_login=1; htVC_2132_connect_is_bind=1; htVC_2132_connect_uin=C93F1A76EC47ECD2A272EB96A7651B4A; htVC_2132_nofavfid=1; htVC_2132_atarget=1; wzws_sessionid=gDExMy44Ny4yMzQuMTAwoGPhy9qCZGIxY2FhgWI5Y2JkOA==; htVC_2132_sid=0; htVC_2132_ttask=1603574%7C20230208; htVC_2132_noticonf=1603574D1D3_3_1; htVC_2132_ulastactivity=1675906394%7C0; htVC_2132_noticeTitle=1; htVC_2132_visitedfid=5D24D2D75D8; htVC_2132_viewid=tid_697540; htVC_2132_st_p=1603574%7C1675906942%7C64a3082dc1ccaa9f52f721fd47dfb7c0; htVC_2132_lastact=1675907124%09plugin.php%09'  # 配置你的cookie
sckey = 'SCT195481Tgi5gISo9TkPb8D3dh2KauAOR' # 配置你的server酱SCKEY

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/"+sckey+".send?text=" + info + "&desp=" + specific,headers=headers)

def main(*args):
    headers={
        'Cookie': cookie,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
