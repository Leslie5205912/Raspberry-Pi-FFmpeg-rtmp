import smtplib
import time
from email.mime.text import MIMEText

def send_mail():
	mail_host = 'smtp.163.com' 
	# smtp服务器地址，如果你不是用163请自行查询
	mail_user = 'Leslie Cheung'  
	# 发信人
	mail_pass = '****'   
	# 邮箱密码(也可能是客户端授权码，我的就是)
	sender = '********@163.com'  
	# 你的邮箱地址
	receivers = '*********@icloud.com'
	# 你想接受到的邮箱地址，qq会被拒收，icloud和gmail都不会
	localtime=time.asctime(time.localtime(time.time()))
	# 推流停止的时间
	message = MIMEText('FFmpeg Failed! %s' % localtime ,'plain','utf-8')
	# 正文，写你想写的
	message['Subject'] = 'Raspberry Message' 
	#标题
	message['From'] = sender 
	message['To'] = receivers  

	try:
	    smtpObj = smtplib.SMTP() 
	    smtpObj.connect(mail_host,25)
	    smtpObj.login(mail_user,mail_pass) 
	    smtpObj.sendmail(
	        sender,receivers,message.as_string()) 
	    smtpObj.quit() 
	    print('success')
	except smtplib.SMTPException as e:
	    print('error',e) 
