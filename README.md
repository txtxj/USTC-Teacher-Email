# USTC 教师邮箱查询

JS 版插件可在此处获取 https://greasyfork.org/zh-CN/scripts/446788

使用方法：

- `pip install -r requirements.txt`

- 在 `config.py` 中填写学号、密码、需要查询的老师姓名
- 运行 `python get_email.py` 

本分支绕过了验证码识别，因此无需安装 `PIL` 等库，但不保证该方案长期有效

可以查看本项目的另一 [`auto_LT`](https://github.com/txtxj/USTC-Teacher-Email/tree/auto_LT) 分支。

目前仅支持根据教师姓名查询，根据课堂号查询还没搞（懒得搞了）

已解决：

~~另外，由于一门课可能有多个老师，所以查询结果可能会有其他老师混进来（也不想搞了）~~

~~另另外，教务系统的登录脚本等一段时间也传一下。~~

---

感谢 [liuly0322](https://github.com/liuly0322) 指出了本项目中的一些问题，这是他的 JavaScript 版 [USTC-Teacher-Email](https://github.com/liuly0322/USTC-Teacher-Email)

感谢 [aysyxx53](https://github.com/aysyxx53) 与 [Kobe972](https://github.com/Kobe972) 为本项目 `login.py` 提供了思路与模板

