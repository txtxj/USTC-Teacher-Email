import re
from bs4 import BeautifulSoup
import requests
import hashlib
from urllib.parse import unquote


class Login:
	def __init__(self, stuid, password):
		self.finepassword = None
		self.fineReportPw = None
		self.session = None
		self.stuid = stuid
		self.password = password
		self.service = u"https%3A%2F%2Fjw.ustc.edu.cn%2Fucas-sso%2Flogin"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
		}

	def passport(self):
		data = self.session.get("https://passport.ustc.edu.cn/login?service=" + self.service, headers=self.headers)
		data = data.text
		data = data.encode("ascii", "ignore").decode("utf-8", "ignore")
		soup = BeautifulSoup(data, "html.parser")
		CAS_LT = soup.find("input", {"name": "CAS_LT"})["value"]
		self.session.get("https://passport.ustc.edu.cn/validatecode.jsp?type=login", stream=True)
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
		return self.session.post("https://passport.ustc.edu.cn/login", data=data, headers=self.headers,
								 allow_redirects=False)

	def login(self):
		self.session = requests.Session()
		ticket = self.passport().headers["Location"]
		rsp = self.session.get(ticket, headers=self.headers).content.decode("utf-8")
		self.fineReportPw = re.search(u"var fineReportPw = '\d+';", rsp)
		self.fineReportPw = re.search("\d+", self.fineReportPw[0])[0]
		self.finepassword = hashlib.md5(self.fineReportPw.encode(encoding="utf-8")).hexdigest()
		params = {
			"fine_username": self.stuid,
			"fine_password": self.finepassword,
			"validity": "-1",
		}
		self.session.get("https://jw.ustc.edu.cn/webroot/decision/login/cross/domain", headers=self.headers, params=params)
		return self.session
