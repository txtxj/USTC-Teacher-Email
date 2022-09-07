# USTC 教师邮箱查询

原仓库由于诸多问题已删除，该仓库为重构后版本

自动登录功能已经实现，不需要再手动填写 `cookies` 

使用方法：

- `pip install -r requirements.txt`

- 在 `config.py` 中填写学号、密码、需要查询的老师姓名
- 运行 `python get_email.py` 

本分支使用了 `Pillow` 和 `pytesseract` 进行了验证码的识别，

如果安装依赖有困难，可以使用本仓库的 [`non_LT`](https://github.com/txtxj/USTC-Teacher-Email/tree/non_LT) 分支。

目前仅支持根据教师姓名查询，根据课堂号查询还没搞（懒得搞了）

### 参考

 - [liuly0322/USTC-Teacher-Email](https://github.com/liuly0322/USTC-Teacher-Email)
 - [aysyxx53](https://github.com/aysyxx53)
 - [Kobe972/USTC-ncov-AutoReport](https://github.com/Kobe972/USTC-ncov-AutoReport)
