import requests
import yaml
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib import parse
import time

from MAIN_CODE.urlArg import UrlArg
from MAIN_CODE.chromeGet import GetChrome


class Elecinfo(UrlArg, GetChrome):

    def __init__(self):
        UrlArg.__init__(self)
        GetChrome.__init__(self)

    def getElecinfo(self):

        page_ = 1
        while True:
            target_url = self.urlParamsSetting(page_=page_)
            self.chromeDriver.get(url= target_url)
            self.chromeDriver.implicitly_wait(3)
            datas = self.chromeDriver.find_elements_by_css_selector("div.cont")

            #-------------------------
            if not datas: break
            #-------------------------
            print("page: {}".format(page_))

            for c, i in enumerate(datas):
                name   = i.find_element_by_css_selector("strong")
                result = i.find_element_by_css_selector("p.l10.t10")
                result_flag = str(result.text).strip().replace(" ","").split("|")

                if result_flag[-1] == "당선":
                    btn = i.find_element_by_css_selector("div.l10.t10 > span:nth-of-type(2) > a")

                    href_url = btn.get_attribute("href")
                    href_url = "http://elecinfo.nec.go.kr/neweps/common/download.do?" + parse.urlparse(href_url).query

                    filename = result_flag[1] +"_"\
                               + result_flag[2] +"_"\
                               + result_flag[3] +"_"\
                               + result_flag[4] +"_"\
                               + result_flag[5] +"_"\
                               + result_flag[6] +"_"\
                               + str(name.text) + "_.pdf"
                    try:
                        urlretrieve(href_url, "C:\\Users\\EZFARM\\PycharmProjects\\NAVER_국회의원\\DOWNLOAD_FILE\\{}".format(filename))
                    except:
                        pass

            page_ = page_ + 1
            time.sleep(5)

        self.chromeDriver.close()

if __name__ == "__main__":
    o = Elecinfo()
    o.getElecinfo()
