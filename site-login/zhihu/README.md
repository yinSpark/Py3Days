# 模拟登录知乎

## 介绍

使用 `requests ` 会话维持模拟，破解加密 JS 文件来模拟登录，验证码需要手动输入。

## 环境

`Node.js` 和 `Python 3+` ，最好使用 Python 虚拟环境

## 安装

```
npm install jsdom
```

```
pip install requests
pip install PyExecJS
pip install lxml
pip install pillow
pip install matplotlib
pip install pyquery
```

## 运行

	python zhihu_login.py

## 维护

如何维护：若出现客户端需要升级错误，请更新参数
	client_id: ''
	x-zse-83: ''
更改加密 `encrypt.js` 文件