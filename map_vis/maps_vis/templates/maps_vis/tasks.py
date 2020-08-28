from invoke import task
import requests
import json

@task
def poi(c):
    '''获取poi'''
    # tags=["美食","酒店","购物","生活服务","丽人","旅游景点","休闲娱乐","运动健身","教育培训",
    # "文化传媒","医疗","汽车服务","交通设施","金融","房地产","公司企业","政府机构","出入口",
    # "自然地物","行政地标","门址"]
    #tags=["房地产","公司企业","政府机构","出入口","自然地物","行政地标","门址"]
    tags = ["房地产"]

    for tag in tags:
        url = "http://api.map.baidu.com/place/v2/search?query="+tag+"&page_size=20&region=北京&city_limit=true&output=json&ak=WuonEjjNztvtKyk3NpVilBd1HkABirTp"
        res = requests.get(url)
        data = res.json()#data是字典形式的，不能用extend追加
        poi = {}
        #poi["tag"] = tag
        #poi["total"] = data["total"]
        #print(data["total"])
        poi["list"] = data['results']
        page_num = int(data['total']/20 + 1)
        print(page_num)


        for i in range(1,page_num+1):
            url = "http://api.map.baidu.com/place/v2/search?query="+tag+"&page_size=20&page_num="+str(i)+"&region=北京&city_limit=true&output=json&ak=WuonEjjNztvtKyk3NpVilBd1HkABirTp"
            #print(url)
            res = requests.get(url)
            poi['list'].extend(res.json()['results'])
        #print("共计"+str(data['total'])+"个"+tag+"poi")
            storedata(tag + 'poi.json', poi)

def storedata(filename, poi):
    filename = filename
    #print(poi)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(poi, f, ensure_ascii=False, indent=4)




