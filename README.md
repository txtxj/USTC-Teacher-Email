# USTC 教师邮箱查询

原仓库由于诸多问题已删除，该仓库为重构后版本

自动登录功能已经实现，不需要再手动填写 `cookies` 

部分代码参考了 liuly0322 的 [USTC-Teacher-Email](https://github.com/liuly0322/USTC-Teacher-Email)

使用方法：

- `pip install -r requirements.txt`

- 在 `config.py` 中填写学号、密码、需要查询的老师姓名
- 运行 `python get_email.py` 

目前仅支持根据教师姓名查询，根据课堂号查询还没搞（懒得搞了）

另外，由于一门课可能有多个老师，所以查询结果可能会有其他老师混进来（也不想搞了）

