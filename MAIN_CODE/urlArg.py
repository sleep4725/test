from urllib.parse import urlencode
import yaml

class UrlArg():

    def __init__(self):
        self.endUrl = UrlArg.getInformation()
        self.encParams = urlencode({
            "epType": "",
            "start_file_sn": "",
            "end_file_sn": "",
            "svc_path_nm": "",
            "epid": "",
            "candidate_nm": "",
            "elect_ymd": "",
            "epdata_id": "",
            "ctl_no_id": "",
            "elect_sn": "",
            "party_nm": "",
            "win_yn": "",
            "elecDe": "",
            "elecType": "20",
            "elecTypeMax": "30",
            "cityType": "EPS042021",
            "sign_id": "21",
            "fieldName": "candidate_nm",
            "category": "tms120tbl",
            "elecTypes": "20",
            "electionType": "on",
            "electionTurn": "on",
            "pageSize": "50",
            "order": "elect_ymd",
            "order_sort": "desc"
        })

    def urlParamsSetting(self, page_):
         return self.endUrl + "turnDe=%B1%B9%C8%B8%C0%C7%BF%F8%BC%B1%B0%C5" +\
                "&" + self.encParams +\
                "&" + "page={}".format(page_) +\
                "&" + "turnType=EPS0420++"+\
                "&" + "code_id=20++"

    @classmethod
    def getInformation(cls):
        try:
            f = open(r"C:\Users\EZFARM\PycharmProjects\NAVER_국회의원\CONFIG\url_info.yml",
                     "r", encoding="utf-8")
        except FileNotFoundError as error:
            print(error)
            return
        else:
            config = yaml.safe_load(f)
            f.close()
            return config.get("url")

