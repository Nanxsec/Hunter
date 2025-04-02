import os
import sys
import re
import requests
import random
import bs4
import hashlib
import json
import string
from urls import *
from headerssites import *
from hunter_style import *

Baner()
sessao = requests.Session()
def get_random_string(quantidade):
	randomico = string.ascii_lowercase
	resultado = ''.join(random.choice(randomico) for i in range(quantidade))
	return(resultado)
async def CheckSitesByEmail(email,armaz=False):
	emails = []
	if sys.platform == "linux":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	Baner()
	print("""
    \033[1;36m#####################################################\033[m
	Buscando pelo email --> \033[1;32m{}\033[m
    \033[1;36m#####################################################\033[m\n""".format(email))
	print("\033[1;33mEsse email está cadastrado em:\n\033[m")
	try:
		wordpress = sessao.get(f"https://public-api.wordpress.com/rest/v1.1/users/{email}/auth-options",timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as e:
		pass
	else:
		if wordpress.status_code == 200:
			resultado_wordpress = json.loads(wordpress.content)
			if str(resultado_wordpress["email_verified"]) == 'True':
				print("\033[1;32m[+] Wordpress.com\033[m")
				emails.append("Wordpress.com")
		else:
			pass
	try:
		imgur = sessao.get("https://imgur.com/register?redirect=%2Fuser",headers=headers_imgur,timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as td:
		pass
	else:
		if imgur.status_code == 200:
			headers_imgur["X-Requested-With"] = "XMLHttpRequest"
			data = {"email":email}
			imgur2 = sessao.post("https://imgur.com/signin/ajax_email_available", headers=headers_imgur, data=data)
			if imgur2.status_code == 200:
				print("\033[1;32m[+] Imgur.com\033[m")
				emails.append("Imgur.com")
			else:
				pass
	try:
		twitter = sessao.get("https://api.twitter.com/i/users/email_available.json",params={"email":email},timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as fd:
		pass
	else:
		if twitter.status_code == 200:
			resultado_twitter = json.loads(twitter.content.decode())
			if str(resultado_twitter["taken"]) == "True":
				print("\033[1;32m[+] Twitter.com\033[m")
				emails.append("Twitter.com")
			else:
				pass
	try:
		pinterest = sessao.get("https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/",
			params={
			"source_url": "/",
			"data": '{"options": {"email": "'+email+'"}, "context": {}}'
			},timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as y:
		pass
	else:
		if pinterest.status_code == 200:
			resultado_pinterest = json.loads(pinterest.text)["resource_response"]["data"]
			if str(resultado_pinterest) == "True":
				print("\033[1;32m[+] Pinterest.com\033[m")
				emails.append("Pinterest.com")
			else:
				pass
	try:
		xvideos = sessao.get("https://www.xvideos.com/account/checkemail",headers=headers_xvideos,params={"email":email},timeout=5)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if xvideos.status_code == 200:
			resultado_xvideos = json.loads(xvideos.content.decode())
			try:
				if "This email is already in use or its owner has excluded it from our website." in str(resultado_xvideos["message"]):
					print("\033[1;32m[+] Xvideos.com\033[m")
					emails.append("Xvideos.com")
				else:
					pass
			except KeyError:
				pass
	try:
		pornhub = sessao.get("https://www.pornhub.com/signup",headers=headers_pornhub,timeout=5)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		varredura_pornhub = bs4.BeautifulSoup(pornhub.content,"html.parser")
		try:
			tokes_find = varredura_pornhub.find(attrs={"name": "token"}).get("value")
		except:
			pass
		else:
			pornhub2 = sessao.post("https://www.pornhub.com/user/create_account_check",
				headers=headers_pornhub,
				params={"token":tokes_find},
				data={"check_what":"email",
				"email":email}
				)
			if pornhub2.status_code == 200:
				response_pornhub = json.loads(pornhub2.content.decode())
				if str(response_pornhub["error_message"]) == "Email has been taken.":
					print("\033[1;32m[+] PornHub.com\033[m")
					emails.append("Pornhub.com")
				else:
					pass
	try:
		xnxx= sessao.get('https://www.xnxx.com', headers=headers_xnxx,timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if xnxx.status_code == 200:
			headers_xnxx['Referer'] = 'https://www.xnxx.com/video-holehe/palenath_fucks_xnxx_with_holehe'
			headers_xnxx['X-Requested-With'] = 'XMLHttpRequest'
			email_xnxx = email.replace('@', '%40')
			xnxx_checks = sessao.get(f'https://www.xnxx.com/account/checkemail?email={email_xnxx}', headers=headers_xnxx, cookies=xnxx.cookies,timeout=10)
			if xnxx_checks.status_code == 200:
				API = json.loads(xnxx_checks.text)
				try:
					if str(API['message']) == 'Cet email est d&eacute;j&agrave; utilis&eacute; ou son propri&eacute;taire l&#039;a exclu de notre site.':
						print("\033[1;32m[+] xnxx.com\033[m")
						emails.append("Xnxx.com")
				except KeyError:
					pass
	try:
		myspace = sessao.get("https://myspace.com/signup/email", headers=headers_myspace)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if myspace.status_code == 200:
			headers_myspace["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
			headers_myspace["X-Requested-With"] = "XMLHttpRequest"
			try:
				myspace2 = sessao.post("https://myspace.com/ajax/account/validateemail",headers=headers_myspace,data={"email":email},timeout=10)
			except:
				pass
			else:
				if myspace2.status_code == 200:
					print("	aao")
					if "This email address was already used to create an account." in str(myspace2.text):
						print("\033[1;32m[+] Myspace.com\033[m")
						emails.append("Myspace.com")
					else:
						print("offline")
	try:
		github = sessao.get("https://github.com/join",headers=headers_github,timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		github_token_regex = re.compile(r'<auto-check src="/signup_check/username[\s\S]?value="([\S]+)"[\s\S]<auto-check src="/signup_check/email[\s\S]*?value="([\S]+)"')
		github_token = re.findall(github_token_regex,github.text)
		try:
			capture_github = sessao.post("https://github.com/signup_check/email",data={"value":email,"authenticity_token":github_token[0]})
		except:
			pass
		else:
			if capture_github.status_code == 200 or capture_github.status_code == 422:
				print("\033[1;32m[+] Github.com\033[m")
				emails.append("Github.com")
			else:
				pass


	try:
		adobe = sessao.post("https://auth.services.adobe.com/signin/v1/authenticationstate",headers=headers_adobe,json={"username": email,"accountType":"individual"},timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		try:
			headers_adobe['X-IMS-Authentication-State-Encrypted'] = adobe.headers['x-ims-authentication-state-encrypted']
		except KeyError:
			pass
		params = {'purpose': 'passwordRecovery',}
		try:
			resposta_adobe = sessao.get("https://auth.services.adobe.com/signin/v2/challenges",headers=headers_adobe,params=params,timeout=10)
		except KeyError:
			pass
		else:
			if "errorCode" not in resposta_adobe.text:
				print("\033[1;32m[+] Adobe.com\033[m")
				emails.append("Adobe.com")

	try:
		docker = sessao.post("https://hub.docker.com/v2/users/signup",headers=headers_docker,data='{"email":"'+email+'","password":"","recaptcha_response":"","redirect_value":"","subscribe":true,"username":""}',timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if "This email is already in use." in str(docker.text):
			print("\033[1;32m[+] Docker.com\033[m")
			emails.append("Docker.com")
		else:
			pass
	try:
		lastpass = sessao.get("https://lastpass.com/create_account.php",params={"check": "avail","skipcontent": "1","mistype": "1","username": email},headers=headers_lastpass,timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as t:
		pass
	else:
		if lastpass.status_code == 200:
			resultado_lastpass = lastpass.text
			if resultado_lastpass != "ok":
				print("\033[1;32m[+]\033[m \033[1mLastpass.com\033[m")
				emails.append("Lastpass.com")
			else:
				pass
	try:
		issuu_site = sessao.get("https://issuu.com/call/signup/check-email/"+email,headers=headers_issuu,timeout=10)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as k:
		print(k)
	else:
		if issuu_site.status_code == 200:
			resultado_issuu_site = json.loads(issuu_site.text())
			if resultado_issuu_site["status"] == "unavailable":
				print("\033[1;32m[+] Issuu.com\033[m")
				emails.append("Issu.com")
			else:
				pass
	try:
		yahoo = sessao.get("https://login.yahoo.com", headers=headers_yahoo)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		headers_yahoo = {
			'User-Agent': "firefox",
			'Accept': '/',
			'Accept-Language': 'en-US,en;q=0.5',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'bucket': 'mbr-fe-merge-manage-account',
			'X-Requested-With': 'XMLHttpRequest',
			'Origin': 'https://login.yahoo.com',
			'DNT': '1',
			'Connection': 'keep-alive',
			}
		params = {
			'.src': 'fpctx',
			'.intl': 'ca',
			'.lang': 'en-CA',
			'.done': 'https://ca.yahoo.com',
		}
		try:
			data = {
				'acrumb': yahoo.text.split('<input type="hidden" name="acrumb" value="')[1].split('"')[0],
				'sessionIndex': yahoo.text.split('<input type="hidden" name="sessionIndex" value="')[1].split('"')[0],
				'username': email,
				'passwd': '',
				'signin': 'Next',
				'persistent': 'y',
			}
			resultado_yahoo = sessao.post('https://login.yahoo.com/',headers=headers_yahoo,params=params,data=data)
			response_hoo = response.json()
			if "error" in response_hoo.keys():
				if not response_hoo["error"]:
					print("\033[1;32m[+] Yahoo.com\033[m")
					emails.append("Yahoo.com")
		except KeyboardInterrupt:
			raise SystemExit
		except:
			pass

	try:
		bodybuilding = sessao.head(f"https://api.bodybuilding.com/profile/email/{email}",headers=headers_bodybuilding)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as gf:
		pass
	else:
		if bodybuilding.status_code == 200:
			print("\033[1;32m[+] Bodybuilding.com\033[m")
			emails.append("Bodybuilding.com")
		else:
			pass
	try:
		soundcloud = sessao.get('https://soundcloud.com/octobersveryown', headers=headers_soundcloud)
		script = bs4.BeautifulSoup(soundcloud.text, 'html.parser').findall('script')[4]
		clientId = json.loads(script.contents[0])["runtimeConfig"]["clientId"]

		linkMail = email.replace('@','%40')
		api_soundclound = sessao.get(f'https://api-auth.soundcloud.com/web-auth/identifier?q={linkMail}&client_id={clientId}',headers=headers_soundcloud)
		response_soundcloud = json.loads(api_soundclound.text)
		if response_soundcloud["status"] == "available" or "in_use":
			print("\033[1;32m[+] SoundCloud.com\033[m")
			emails.append("SoundClound.com")
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass

	try:
		spotify = sessao.get("https://spclient.wg.spotify.com/signup/public/v1/account",headers=headers_spotify,params={"validate": "1","email": email})
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if spotify.status_code == 200:
			response_spotify = json.loads(spotify.text)
			if response_spotify["status"] == 20:
				print("\033[1;32m[+] Spotify.com\033[m")
				emails.append("Spotify.com")
			else:
				pass
	try:
		data = {
			'referringUrl': '',
			'genpass': '1',
			'signup[urlName]': 'test',
			'signup[emailAddress]': email,
			'g-recaptcha-response': '',
			'tos': '0'
		}
		blip = sessao.post("https://blip.fm/signup/save",headers=headers_blip,data=data)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if "That email address is already in use." in blip.text:
			print("\033[1;32m[+] Blip.fm\033[m")
			emails.append("Blip.fm")
		else:
			pass
	try:
		smule = sessao.get("https://www.smule.com/user/check_email", headers=headers_smule)
		token = smule.text.split('authenticity_token" name="csrf-param" />\n<meta content="')[1].split('"')[0]
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		headers_smule["X-CSRF-Token"] = str(token)
		smule_2 = sessao.post('https://www.smule.com/user/check_email', headers=headers_smule, data={"email": str(email)})
		if str(smule_2.json()["email"]) == True:
			print("\033[1;32m[+] Smule.com\033[m")
			emails.append("Smule.com")
		else:
			pass
	try:
		params = {
			'appVersion': '831',
			'experienceVersion': '831',
			'uxid': 'com.nike.commerce.nikedotcom.web',
			'locale': 'fr_FR',
			'backendEnvironment': 'identity',
			'browser': '',
			'mobile': 'false',
			'native': 'false',
			'visit': '1',
		}
		nike = sessao.post("https://unite.nike.com/account/email/v1",headers=headers_nike,param=params,data='{"emailAddress":'+email+'}')
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if nike.status_code == 409:
			print("\033[1;32m[+] Nike.com\033[m")
			emails.append("Nike.com")
		else:
			pass
	try:
		rockethree = sessao.get("https://rocketreach.co/signup")
		tokenr = re.search(r'name="csrfmiddlewaretoken" value="(.*)"',rockethree.text).group(1)
		headers_rock["x-csrftoken"] = tokenr
	except:
		pass
	else:
		try:
			rock1 = sessao.get('https://rocketreach.co/v1/validateEmail?email_address='+email,headers_rock)
		except KeyboardInterrupt:
			raise SystemExit
		except:
			pass
		else:
			response_rock = str(rock1.json()["found"])
			if response_rock == "True":
				print("\033[1;32m[+] Rocketreach.co\033[m")
				emails.append("Rocketreach.com")
			else:
				pass
	try:
		freelancer = sessao.post('https://www.freelancer.com/api/users/0.1/users/check?compact=true&new_errors=true',data='{"user":{"email":"' + email + '"}}',headers=headers_free)
		resdata = freelancer.json()
		if freelancer.status_code == 409 and "EMAIL_ALREADY_IN_USE" in freelancer.text:
			print("\033[1;32m[+] Freelancer.com\033[m")
			emails.append("Freelancer.com")
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass

	try:
		response_zoho = sessao.get("https://accounts.zoho.com/register", headers=headers_zoho)
		headers_zoho['X-ZCSRF-TOKEN']='iamcsrcoo='+response.cookies["iamcsr"]
		data = {
			'mode': 'primary',
			'servicename': 'ZohoCRM',
			'serviceurl': 'https://crm.zoho.com/crm/ShowHomePage.do',
			'service_language': 'fr',
		}
		reponse_zoho = sessao.post('https://accounts.zoho.com/signin/v2/lookup/'+email, headers=headers_zoho, data=data)
		if response_zoho.status_code == 200 and "message" in response_zoho.js:
			print("\033[1;32m[+] Zoho.com\033[m")
			emails.append("Zoho.com")
		else:
			pass
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass

	try:
		headers_duolingo = {
			'authority': 'www.duolingo.com',
			'method': 'GET',
			'path': '/2017-06-30/users?email=' +email,
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8',
			'Accept-Encoding': 'gzip, deflate, br, zstd',
			'Accept-Language': 'en-US,en;q=0.8',
			'User-Agent': "firefox",
		}
		duolingo = sessao.get("https://www.duolingo.com/2017-06-30/users?email="+email,headers=headers_duolingo)
	except KeyboardInterrupt:
		raise SystemExit
	except Exception as ggf:
		pass
	else:
		response_duolingo = duolingo.json()
		if response_duolingo["users"]:
			print("\033[1;32m[+] Duolingo.com\033[m")
			emails.append("Duolingo.com")
		else:
			pass
	try:
		cookies = {
			'lang': 'en_US',
			'showSurvey': 'true',
			'cookiesEnabled': 'true',
		}
		data = {
			'csrf': '',
			'email': email,
			'password_placeholder': '',
			'submit-btn': 'Continue'
		}

		cari = sessao.post('https://www.caringbridge.org/signin', headers=headers_cari, cookies=cookies, data=data, timeout=3)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	if "Welcome Back," in cari.text:
		print("\033[1;32m[+] Caringbridge.org\033[m")
		emails.append("Caringbridge.org")
	else:
		pass

	try:
		coffee = sessao.get("https://www.buymeacoffee.com/", headers=headers_coffee)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if coffee.status_code == 200:
			try:
				soup = BeautifulSoup(coffee.content, features="html.parser")
				csrf_token = soup.find(attrs={'name': 'bmc_csrf_token'}).get("value")
			except KeyboardInterrupt:
				raise SystemExit
			except AttributeError:
				pass
			else:
				if csrf_token:
					cookies = {
						'bmccsrftoken': csrf_token,
					}
					data = {
						'email': email,
						'password': get_random_string(20),
						'bmc_csrf_token': csrf_token
					}
					coffee2 = sessao.post('https://www.buymeacoffee.com/auth/validate_email_and_password',headers=headers_coffee,cookies=cookies,data=data)
					if coffe2.status_code == 200:
						coffee_ingredients = coffe2.json()
						if coffee_ingredients["status"] == "SUCCESS":
							print("\033[1;32m[+] Buymeacoffee.com\033[m")
							emails.append("Buymeacoffee.com")
						else:
							pass
		else:
			pass
	try:
		diigo = sessao.get("https://www.diigo.com/user_mana2/check_email", headers=headers_diigo, params={"email": email})
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if diigo.status_code == 200:
			if diigo.text == "0":
				print("\033[1;32m[+] Diigo.com\033[m")
			else:
				pass
	try:
		data = '{"fingerprint":"","email":"' + str(email) + '","username":"' + get_random_string(20) + '","password":"' + get_random_string(20) + '","invite":null,"consent":true,"date_of_birth":"","gift_code_sku_id":null,"captcha_key":null}'
		discord = sessao.post("https://discord.com/api/v8/auth/register",headers=headers_discord,data=data)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		response_discord = discord.json()
		try:
			if "code" in response_discord.keys():
				try:
					if responseData["errors"]["email"]["_errors"][0]['code'] == "EMAIL_ALREADY_REGISTERED":
						print("\033[1;32m[+] Discord.com\033[m")
						emails.append("Discord.com")
					else:
						pass
				except KeyboardInterrupt:
					raise SystemExit
				except:
					pass
		except KeyboardInterrupt:
			raise SystemExit
		except:
			pass
	try:
		params = {
			'email': str(email),
			'errorMessage': '',
			'limit': '25',
		}
		tellonym = sessao.get('https://api.tellonym.me/accounts/check', headers=headers_tell, params=params)
	except KeyboardInterrupt:
		raise SystemExit
	except:
		pass
	else:
		if "EMAIL_ALREADY_IN_USE" in tellonym.text:
			print("\033[1;32m[+] Tellonym.me\033[m")
			emails.append("Tellonym.me")
		else:
			pass
	if armaz:
		for sites_found in emails:
			with open("Emails.txt","a") as save:
				save.write("{} Tem conta em: {}\n".format(email,sites_found))
			save.close()
		with open("Emails.txt","a") as save2:
			save2.write("---------------------------------------------\n\n")
		save2.close()
