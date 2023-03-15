import urllib.request
# import smtplib, ssl
from configparser import ConfigParser

from json import dumps

config = ConfigParser()
config.read('./envfile.ini')

# smtp_server = 'smtp.mail.yahoo.com'
# sender_email = 'robynfhveitch@yahoo.com'
# receiver_email = 'robynfhveitch@gmail.com'
# # port = 465
# port = 587
# password = config['DEFAULT']['PASSWORD']
# message = """\
# Subject: Hi there

# This message is sent from Python."""

def foo(world):
	return { 'hello': world }

def test_snapshot_ability(snapshot):
	snapshot.snapshot_dir = 'snapshots'
	snapshot.assert_match(dumps(foo('world')), 'foo_output.txt')

def test_index_against_snapshot(snapshot):
	snapshot.snapshot_dir = 'snapshots'

	with urllib.request.urlopen('https://robynveitch.com/') as response:
		assert response.status == 200
		html = response.read().decode('utf-8')
		snapshot.assert_match(html, 'robynveitchcom_index.txt')


def test_blog_exists():
	with urllib.request.urlopen('https://robynveitch.com/blog') as response:
		assert response.status == 200


def test_cv_exists(snapshot):
	snapshot.snapshot_dir = 'snapshots'

	with urllib.request.urlopen('https://robynveitch.com/robyn-veitch-cv/') as response:
		assert response.status == 200
		html = response.read().decode('utf-8')
		snapshot.assert_match(html, 'robynveitchcom_cv.txt')

	# OPTIONAL: check SSL and vulnerabilities
	# with urllib.request.urlopen('https://www.ionos.com/api/ssl-checker?domain=robynveitch.com') as response:
	# 	assert response.status == 200
	# 	print(response)
	# 	print(str(response))
		
# try:
# 	print('...attempting')
# 	print(ssl.OPENSSL_VERSION)
# 	context = ssl.create_default_context()
# 	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# 		print('...server init')
# 		server.login(sender_email, password)
# 		print('login finished')
# 		server.sendmail(sender_email, receiver_email, message)
# 		print('email sent')
# except Exception as ex:
# 	print('error')
# 	print(str(ex))