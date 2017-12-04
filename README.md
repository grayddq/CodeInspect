# CodeInspect 0.1

这个脚本的主要目标是根据代码发布的方式，从根本上实现WEBShell、网马或恶意链接等安全方面的检测。


## Support ##

满足如下安全需求

	1、周期内查询网站代码是否进行过修改如：添加、修改
	2、修改的文件进行日志告警、并进行提取备份
	3、事件发生时，立即进行代码同步恢复，删掉添加和修改的内容。

技术细节如下：

	1、支持GIT、SVN、Rsync等代码发布服务


## Test Environment ##

>CentOS Linux release 7.3.1611 (Core)

## Tree ##

	PubilcAssetInfo
	----CodeInspect.py   #主程序
	

## Config ##

配置信息：./conf/info.conf

	# 代码路径
	CODE_DIR_LIST = ['/root/tool/PubilcAssetInfo', '/home/seclogin/test_gdd/testbbb', '/home/seclogin/test_gdd/testrsync']
	# 代码同步方式 git / svn / rsync
	TYPE = 'rsync'
	# 是否执行代码恢复，True / False
	ACTION = True
	# 可疑文件存放的地方
	TMP = '/tmp/codeinspect/'
	# rsync服务的登录,替换其中的IP、账户、密码文件
	RSYNC_LOGIN_INFO = 'rsync --password-file=/etc/pass.txt test@192.168.1.5::web'

## Log ##

日志目录默认：/var/log/codeinspect.log


## Screenshot ##

![Screenshot](pic/111.png)

## output ##

默认可疑文件：/tmp/codeinspect/

## Author ##
咚咚呛 