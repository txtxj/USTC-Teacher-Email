class Login:
	def __init__(self, stuid, password):
		self.url = "https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fjw.ustc.edu.cn%2Fucas-sso%2Flogin"
		self.cookies = None
		self.sid = stuid
		self.pwd = password

	def login(self):
		# TODO: Use sid and pwd to get the cookies of jwc. The cookies should be stored in self.cookies
		pass