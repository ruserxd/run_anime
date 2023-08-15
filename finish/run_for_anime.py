print("抓取最新動畫!")
print("-----------")
#引入
import urllib.request as req
#網址
url ="https://ani.gamer.com.tw/"
#需求
request = req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})
#讀取
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#引入
import bs4
#使用bs4
root =bs4.BeautifulSoup(data,"html.parser")
titles = root.find_all("div",class_="anime-name")

#操作
k = 1
lst1 ={}
for t in titles:
    if t.p != None :
        if t.p.string not in lst1:
            print(k,t.p.string)
            #判斷有沒有重複的字典
            lst1[t.p.string] =k
            k+=1
