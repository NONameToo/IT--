# -*- coding: utf-8 -*-
import scrapy

# from scrapy_redis.spiders import RedisSpider

from itjuzi.items import ItjuziItem
import json
import jsonpath
import random
# class CompanySpider(scrapy.Spider):
class CompanySpider(scrapy.Spider):
    name = 'company'
    #allowed_domains = ['radar.itjuzi.com']
    items = []

    # redis_key = 'companyspider:start_urls'
    # start_urls = ['http://radar.itjuzi.com/company/infonew?page='+str(offset)+'&scope%5B%5D=1&scope%5B%5D=12&scope%5B%5D=28&scope%5B%5D=38&scope%5B%5D=47&scope%5B%5D=57&scope%5B%5D=70&scope%5B%5D=80&scope%5B%5D=95&scope%5B%5D=103&scope%5B%5D=115&scope%5B%5D=126&scope%5B%5D=135&scope%5B%5D=145&scope%5B%5D=161&scope%5B%5D=210&scope%5B%5D=211&scope%5B%5D=258']
    # url ='http://radar.itjuzi.com/company/infonew?page='+str(offset)+'&scope%5B%5D=1&scope%5B%5D=12&scope%5B%5D=28&scope%5B%5D=38&scope%5B%5D=47&scope%5B%5D=57&scope%5B%5D=70&scope%5B%5D=80&scope%5B%5D=95&scope%5B%5D=103&scope%5B%5D=115&scope%5B%5D=126&scope%5B%5D=135&scope%5B%5D=145&scope%5B%5D=161&scope%5B%5D=210&scope%5B%5D=211&scope%5B%5D=258'
    cookies = {
        "Hm_lvt_1c587ad486cdb6b962e94fc2002edf89": "1537774442",
        "gr_user_id": "1bf4f95b-ef32-4d51-831a-ee4cf4f5a8e7",
        "_ga": "GA1.2.1479080892.1537774443",
        "_gid": "GA1.2.1185425853.1537774443",
        "identity": "1076796244%40qq.com",
        "remember_code": "gqZjR3Pff2",
        "unique_token": "642072",
        "paidtype": "vip",
        "acw_tc": "781bad0615377765547388476e679864567785467ec346642789595fe678aa",
        "user-radar.itjuzi.com": "%7B%22n%22%3A%22%5Cu6854%5Cu53cb42a112d44ee83%22%2C%22v%22%3A2%7D",
        "Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b": "1537776551",
        "MEIQIA_VISIT_ID": "1Ae5ukytMpAqbbQP8R3nkxOJObS",
        "MEIQIA_EXTRA_TRACK_ID": "1Ae5um7U34aC70eBMAvPbzkkxVj",
        "Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b": "1537778541",
        "gr_session_id_eee5a46c52000d401f969f4535bdaa78": "cbfc85a5-3a84-470b-9cfe-4c246b3031e6",
        "gr_cs1_cbfc85a5-3a84-470b-9cfe-4c246b3031e6": "user_id%3A642072",
        "session": "02e75bd90d1bd1a801de3601ea3499a20365ab6d",
        "Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89": "1537780294",
        "gr_session_id_eee5a46c52000d401f969f4535bdaa78_cbfc85a5-3a84-470b-9cfe-4c246b3031e6": "true",

    }

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
        "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]

    headers = {

        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": random.choice(user_agent_list),

    }

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))

        # 修改这里的类名为当前类名
        super(CompanySpider, self).__init__(*args, **kwargs)




    def start_requests(self):
        # for j in range(30):
        #     yield scrapy.FormRequest('http://radar.itjuzi.com/company/infonew?page=' + str(1) + '&scope%5B%5D=1&scope%5B%5D=12&scope%5B%5D=28&scope%5B%5D=38&scope%5B%5D=47&scope%5B%5D=57&scope%5B%5D=70&scope%5B%5D=80&scope%5B%5D=95&scope%5B%5D=103&scope%5B%5D=115&scope%5B%5D=126&scope%5B%5D=135&scope%5B%5D=145&scope%5B%5D=161&scope%5B%5D=210&scope%5B%5D=211&scope%5B%5D=258', cookies=self.cookies, headers=self.headers)


        # print(self.urls)
        for i in range(5000):
            yield scrapy.FormRequest('http://radar.itjuzi.com/company/infonew?page='+str(i+1)+'&scope%5B%5D=1&scope%5B%5D=12&scope%5B%5D=28&scope%5B%5D=38&scope%5B%5D=47&scope%5B%5D=57&scope%5B%5D=70&scope%5B%5D=80&scope%5B%5D=95&scope%5B%5D=103&scope%5B%5D=115&scope%5B%5D=126&scope%5B%5D=135&scope%5B%5D=145&scope%5B%5D=161&scope%5B%5D=210&scope%5B%5D=211&scope%5B%5D=258', cookies=self.cookies, callback=self.parse_page, headers=self.headers)

            # 发送详细页的请求
            for item in self.items:
                # print(item)
                yield scrapy.FormRequest("http://www.itjuzi.com/company/"+item['company_id'], cookies=self.cookies, meta={'meta1': item}, callback=self.parse_detail, headers=self.headers)
            self.items = []

        # self.offset += 1






    def parse_page(self, response):

        # 把json数据转换成Python对象
        company_list = json.loads(response.body.decode('utf-8'))
        # 总共有多少页：
        page_count = jsonpath.jsonpath(company_list, '$..data')[0]['page_total']
        print(page_count)

        # 当前第几页：
        now_page = jsonpath.jsonpath(company_list, '$..data')[0]['page_num']
        print(now_page)

        companys = jsonpath.jsonpath(company_list, '$..rows')[0]


        for company in companys:


            item = ItjuziItem()


            # 解析想要的字段：
            item["company_name"] = company["com_name"]
            # logo地址
            item["company_logo"] = company['com_logo_archive']

            # 公司id
            item['company_id'] = company['com_id']
            # 公司描述
            item["company_des"] = company['com_des']
            # 公司行业
            item["company_fa"] = company['com_cat_name']
            # 公司子行业
            item["company_son"] = company['com_sub_cat_name']

            # 最新融资情况由四步分组成：
            invse_date = company['invse_date']
            invse_round_id = company['invse_round_id']
            invse_detail_money = company['invse_detail_money']
            invse_total_money = company['invse_total_money']

            # 公司最新融资情况
            item["company_recent"] = invse_date+' '+invse_round_id+' '+invse_detail_money+' '+invse_total_money
            # 公司资产总额
            item["company_count"] = company['invse_total_money']
            # 公司估价
            item["company_money"] = company['guzhi']

            # 公司地址
            item['company_addr'] = company['com_addr']
            # 公司标语
            item['company_slogan'] = company['com_slogan']


            # 公司成立时间
            item["company_btime"] = company['com_born_date']
            # 公司规模
            item["company_people"] = company['com_scale']
            # 公司营运情况
            item["company_operate"] = company['com_status']


            self.items.append(item)



    # 解析详细页
    def parse_detail(self, response):
        print("6666666666666666666666666666")
        # print(response.body)

        item = response.meta["meta1"]

        # 详细页里面的
        # 公司全名
        item["company_fullname"] = response.xpath('//div[@class="des-more"]/h2/text()').extract()[0]
        # 团队人员姓名
        item["perosonname"] = response.xpath('//div[@class="sec"]//a[@class="person-name"]/text()').extract()[0]
        # 职位
        item["perosonposition"] = response.xpath('//div[@class="sec"]//div[@class="per-position"]/text()').extract()[0]
        # 个人简介
        item["perosondes"] = response.xpath('//div[@class="sec"]//div[@class="per-des"]/div/text()').extract()[0].strip()
        # 公司产品
        item["product"] = response.xpath('//div[@class="sec panel-for-scroll"]//div[@class="product-list empty-list empty-with-link"]/div/text()').extract()[0]
        print(item)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        yield item










        
        # print(response.body.decode('utf-8'))
        # print(company_list)

