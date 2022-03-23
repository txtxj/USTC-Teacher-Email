import re
from bs4 import BeautifulSoup
import requests
import hashlib
from urllib.parse import unquote

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


class Login:
	def __init__(self, stuid, password):
		self.finepassword = None
		self.fineReportPw = None
		self.session = None
		self.result = None
		self.cookies = None
		self.stuid = stuid
		self.password = password
		self.service = u"https%3A%2F%2Fjw.ustc.edu.cn%2Fucas-sso%2Flogin"

	# Due to a bug of passport.ustc.edu.cn, the LT is not necessary.
	# To avoid inputting the LT field, just get the picture and return nothing.
	def get_LT(self):
		self.session.get("https://passport.ustc.edu.cn/validatecode.jsp?type=login", stream=True)

	def passport(self):
		data = self.session.get("https://passport.ustc.edu.cn/login?service=" + self.service, headers=headers)
		data = data.text
		data = data.encode("ascii", "ignore").decode("utf-8", "ignore")
		soup = BeautifulSoup(data, "html.parser")
		CAS_LT = soup.find("input", {"name": "CAS_LT"})["value"]
		self.get_LT()
		data = {
			"model": "uplogin.jsp",
			"service": unquote(self.service),
			"warn": "",
			"showCode": "1",
			"username": self.stuid,
			"password": str(self.password),
			"button": "",
			"CAS_LT": CAS_LT,
			"LT": "",
		}
		self.result = self.session.post("https://passport.ustc.edu.cn/login", data=data, headers=headers,
										allow_redirects=False)

	def login(self):
		self.session = requests.Session()
		self.passport()
		ticket = self.result.headers["Location"]
		rsp = self.session.get(ticket, headers=headers).content.decode("utf-8")
		self.fineReportPw = re.search(u"var fineReportPw = '\d+';", rsp)
		self.fineReportPw = re.search("\d+", self.fineReportPw[0])[0]
		self.finepassword = hashlib.md5(self.fineReportPw.encode(encoding="utf-8")).hexdigest()
		params = {
			"fine_username": self.stuid,
			"fine_password": self.finepassword,
			"validity": "-1",
		}
		self.session.get("https://jw.ustc.edu.cn/webroot/decision/login/cross/domain", headers=headers, params=params)
		return self.session
