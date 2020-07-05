from selenium import webdriver

class GetChrome:

    def __init__(self):
        self.chromeDriver = GetChrome.getChromeClient()

    @classmethod
    def getChromeClient(cls):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        chrome_option.add_argument("window-size=1920x1080")
        chrome_option.add_argument("disable-gpu")

        ## =======================================================================================
        # download_dir = "C:\\Users\\EZFARM\\PycharmProjects\\NAVER_국회의원\\DOWNLOAD_FILE\\"  # for linux/*nix, download_dir="/usr/Public"
        # options = webdriver.ChromeOptions()
        #
        # profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        #            # Disable Chrome's PDF Viewer
        #            "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
        # options.add_experimental_option("prefs", profile)
        ## =======================================================================================

        chromeClient = webdriver.Chrome("C:/Users/EZFARM/PycharmProjects/NAVER_국회의원/CONFIG/chromedriver.exe",
                                        chrome_options =chrome_option)

        return chromeClient