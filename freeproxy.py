import requests

good_proxy = []

with open('proxy.txt','r') as f:
    proxy_list_all=f.read().split('\n')

#print(proxy_list_all[0])

for i in proxy_list_all:
    proxies = {"http": 'http://'+i,"https://": 'https'+i}
    #print(proxies)
    try:
        response=requests.get('http://httpbin.org/ip',proxies=proxies)
        #print(i+'='+response.content)
        print(response.content)
        good_proxy.append(i)
        
    except:
        pass
        #print('Failed.')
print(good_proxy)
