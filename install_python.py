#coding=utf-8

import os
import sys

if os.getuid()==0:
	pass
else:
	print "当前用户不是root用户，请用root用户执行脚本。"
	sys.exit(1)

version = raw_input("请输入你想安装的python版本(2.7/3.8)：")


if "linux" in sys.platform:
	if version == "2.7":
	        url="https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz"
		package_name = "Python-2.7.18"
	elif version == "3.8":
	        url = "https://www.python.org/ftp/python/3.8.4/Python-3.8.4.tgz"
		package_name = "Python-3.8.4"
	else:
	        print "您输入的版本号有误，请输入2.7或3.8。"
	cmd = "yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel"
	res = os.system(cmd)
	if res != 0:
		print "依赖安装失败！"
                sys.exit(1)
	cmd = "wget "+url
	res = os.system(cmd)
	if res != 0:
	        print "下载源码包失败，请检查网络"
		sys.exit(1)
	cmd="tar -zxvf" + package_name + ".tgz"
	res = os.system(cmd)
	if res!=0:
		os.system("rm -rf "+package_name+".tgz")
		print "解压源码包失败，请重新运行这个脚本现在源码包"
		sys.exit(1)
	cmd="cd "+package_name+" && ./configure --prefix=/usr/local/python3 && make && make install"
	res = os.system(cmd)
	if res!=0:
		print "编译python源码失败，请检查是否缺少依赖库"
		sys.exit(1)
if "win" in sys.platform:
	if version == "2.7":
	        url="https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi"
		package_name = "python2.7.18.amd64.msi"
	elif version == "3.8":
	        url = "https://www.python.org/ftp/python/3.8.4/python-3.8.4.exe"
		package_name = "python-3.8.4.exe"
	else:
	        print "您输入的版本号有误，请输入2.7或3.8。"
	cmd = "client = new-object System.Net.WebClient"
	if res != 0:
		print "WebClient执行失败。"
		sys.exit(1)
	cmd = "client.DownloadFile("+url+"C:\\Users\\username\\Desktop\\"+package_name
	res = os.system(cmd)
	if res!=0:
		print "下载源码包失败，请检查网络"
                sys.exit(1)




