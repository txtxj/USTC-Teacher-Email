from config import POOL, TEACHER_NAME
import requests
import json
import re


class Lesson:
	def __init__(self, cookies):
		self.lesson_id = []
		self.email = None
		self.teacher_name = TEACHER_NAME.split(" ")
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
			"cookie": cookies
		}

	def get_lesson_id(self):
		sn = re.findall("\d+", requests.get(url="https://jw.ustc.edu.cn/for-std/lesson-search", headers=self.headers).url)[0]
		for name in self.teacher_name:
			for p in POOL:
				source = "https://jw.ustc.edu.cn/for-std/lesson-search/semester/{}/search/{}?teacherNameLike={}".format(p, sn, name)
				rsp = requests.get(url=source, headers=self.headers)
				result = json.loads(rsp.content.decode("utf-8"))
				if len(result["data"]) == 0:
					continue
				else:
					self.lesson_id.append(result["data"][0]["id"])
					break

	def find_all(self):
		self.get_lesson_id()
		email_list = []
		for tid in self.lesson_id:
			url = "https://jw.ustc.edu.cn/ws/course-adjustment-apply/get-teacher-info?lessonId={}".format(tid)
			rsp = requests.get(url, headers=self.headers)
			email_list.append(rsp.content.decode("utf-8"))
		return email_list

