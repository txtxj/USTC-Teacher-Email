# USTC 教师邮箱查询

原仓库由于诸多问题已删除，该仓库为重构后版本

自动登录功能尚未实现，需要手动填写 `cookies` 

部分代码参考了 lly0322 的 [USTC-Tercher-Email](https://github.com/liuly0322/USTC-Tercher-Email)

使用方法：

- `pip install -r requirements.txt`

- 在 `config.py` 中填写学号、密码、需要查询的老师姓名
- 获取 `cookies` ，有以下方法
  - 在 `login.py` 中填写你的代码，自动获取 `cookies` 
  - 在浏览器中登录，在 检查-网络 中找到一个带 `cookie` 的请求，将 `cookie` 复制到 `login.py` 中，赋值给 `self.cookies` 
- 运行 `python get_email.py` 

目前仅支持根据教师姓名查询，根据课堂号查询还没搞（懒得搞了）

另外，由于一门课可能有多个老师，所以查询结果可能会有其他老师混进来（也不想搞了）

自动登录脚本 `login.py` 已经在鹿上了
