import requests
import os
import time
from bs4 import BeautifulSoup as BS

RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'

def get_html(url):
	return requests.get(url).text

def parse_ua(tutilka):
	soup = BS(tutilka, 'html.parser')
	for date in soup.findAll('td'):
		content = date.getText().split('  ')
		for g in content:
			if g == '':
				pass
			elif '\n' in g:
				g = g.replace("\n", "")
			else:
				print(f'{CYAN}[{RED}*{CYAN}] {GREEN}'+g)

print(f'''{BOLD}\033[35m    ░░░░░░░▄███▄▄▄░░▄▄▄███▄ ░░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ██▄▄▄██▀▀▀▀██████████▀▀▀▀██▄▄▄██
    ░▀██████▄▄▄░░░░░░░░░░▄▄▄██████▀░
    ░░░▀████████████████████████▀░░░
    ░░▄█▀█▀▀▀▀████████████▀▀▀▀█▀█▄░░
    ░░█▀░▀░░░░░▄▄░░░░░░▄▄░░░░░▀░▀█░░
    ░░█▄░░░░░░█░░█░░░░█░░█░░░░░░▄█░░
    ░░░▀██▄░░░░▀▀░░█░░░▀▀░░░░▄██▀░░░
    ░░░░░▀█▄░░░░░░░▀▀░░░░░░░▄█▀░░░░░
    ░░░░░░░██▄▄░░░████░░░▄▄██░░░░░░░
    ░░░░░▄███████▄▄▄▄▄▄███████▄░░░░░
    ░░░░▄██████████████████████▄░░░░
    ░░░▄████████████████████████▄░░░
    ░░▄██████████████████████████▄░░
    
{CYAN}[{RED}1{CYAN}] Car Scan (UK)   [{RED}2{CYAN}] Инфа по номеру [{RED}3{CYAN}] Инфа по IP
[{RED}4{CYAN}] TorrentScan     [{RED}5{CYAN}] Parse Proxy  [{RED}6{CYAN}] Авито сканер
                    [{RED}7{CYAN}] BSSID Locate
[{RED}!{CYAN}] Run with proxy or VPN.
[{RED}*{CYAN}] Made by {GREEN}@tenych69{CYAN} Telegram: {GREEN}@termuxmam (Subscribe) {CYAN}
''')

while True:
	shell = input(f'{CYAN}[{RED}*{CYAN}] Choose number: {GREEN}')
	if shell == '1':
		num = input(f'{CYAN}[{RED}*{CYAN}] Car-Number: {GREEN}')
		parse_ua(get_html('https://baza-gai.com.ua/nomer/' + num))
	elif shell == '2':
		phone = input(f'{CYAN}[{RED}*{CYAN}] Номер телефона: {GREEN}')
		try:
			response = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone)
			data = response.json()
			user_country = data[ 'country' ][ 'english' ]
			user_id = data[ 'country' ][ 'id' ]
			user_location = data[ 'country' ][ 'location' ]
			user_city = data[ 'capital' ][ 'english' ]
			user_lat = data[ 'capital' ][ 'latitude' ]
			user_log = data[ 'capital' ][ 'longitude' ]
			user_post = data[ 'capital' ][ 'post' ]
			user_oper = data[ '0' ][ 'oper' ]
			uty = requests.get("https://api.whatsapp.com/send?phone="+phone)
			if uty.status_code==200:
				utl2 = "https://api.whatsapp.com/send?phone="+phone
			else:
				utl2 = 'Not founded!'
			userr_all_info = f'{CYAN}[{RED}*{CYAN}] Country: {GREEN}{str(user_country)}\n{CYAN}[{RED}*{CYAN}] ID: {GREEN}{str(user_id)}\n{CYAN}[{RED}*{CYAN}] Location: {GREEN}{str(user_location)}\n{CYAN}[{RED}*{CYAN}] City: {GREEN}{str(user_city)}\n{CYAN}[{RED}*{CYAN}] Latitude: {GREEN}{str(user_lat)}\n{CYAN}[{RED}*{CYAN}] Longitude:{GREEN} {str(user_log)}\n{CYAN}[{RED}*{CYAN}] Index post:{GREEN} {str(user_post)}\n{CYAN}[{RED}*{CYAN}] Operator:{GREEN} {str(user_oper)}'
			num_name = []
			phone_ow = requests.get(f'https://phonebook.space/?number=%2B{phone}').text
			content = BS(phone_ow, 'html.parser').find('div', class_='results')
			for i in content.find_all('li'):
				num_name.append(i.text.strip())
			name = ', '.join(num_name)
			user_all_info = f"""
\033[35m-===[Operator Info]===-
{userr_all_info}
\033[35m-===[Social Networks]===-
{CYAN}[{RED}*{CYAN}] WhatsApp: {GREEN}{utl2}
\033[35m-===[Personal Info]===-
{CYAN}[{RED}*{CYAN}] Possible names: {GREEN}{name}
	"""
			print(user_all_info)
		except:
			print(f'{CYAN}[{RED}-{CYAN}] Хуево написал, пиши правильнее. ¯╲_(ツ)_/¯')
	elif shell == '3':
		query = input(f'{CYAN}[{RED}*{CYAN}] Ip For Scan: {GREEN}')
		try:
			r = requests.get(f'http://ip-api.com/json/{query}').json()
			print(f'{CYAN}[{RED}*{CYAN}] Country:{GREEN} {r["country"]}\n{CYAN}[{RED}*{CYAN}] CountryCode:{GREEN} {r["countryCode"]}\n{CYAN}[{RED}*{CYAN}] Region:{GREEN} {r["region"]}\n{CYAN}[{RED}*{CYAN}] Region Name:{GREEN} {r["regionName"]}\n{CYAN}[{RED}*{CYAN}] City: {GREEN}{r["city"]}\n{CYAN}[{RED}*{CYAN}] Zip:{GREEN} {r["zip"]}\n{CYAN}[{RED}*{CYAN}] Latinude: {GREEN}{r["lat"]}\n{CYAN}[{RED}*{CYAN}] Longitude: {GREEN}{r["lon"]}\n{CYAN}[{RED}*{CYAN}] Timezone: {GREEN}{r["timezone"]}\n{CYAN}[{RED}*{CYAN}] ISP:{GREEN} {r["isp"]}\n{CYAN}[{RED}*{CYAN}] Org:{GREEN} {r["org"]}\n{CYAN}[{RED}*{CYAN}] As: {GREEN}{r["as"]} ')
		except:
			print(f'{CYAN}[{RED}-{CYAN}] Не найдено, либо ты гей :)')
	elif shell == '4':
		query = input(f'{CYAN}[{RED}*{CYAN}] Ip For Scan: {GREEN}')
		target_ip = query
		try:
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36","Connection": "keep-alive","Host": "iknowwhatyoudownload.com","Referer": "https://iknowwhatyoudownload.com"}
			page = requests.get("https://iknowwhatyoudownload.com/ru/peer/?ip=" + target_ip, headers=headers)
			soup = BS(page.content, "html.parser")
			table = soup.find(class_="table").find("tbody")
			torrents = table.find_all("tr")
			for torrent in torrents:
				first, last = torrent.find_all(class_="date-column")
				first, last = first.text, last.text
				category = torrent.find(class_="category-column").text
				name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
				size = torrent.find(class_="size-column").text
				print(f'{CYAN}[{RED}*{CYAN}] Использовано первый раз: {GREEN}{first}{CYAN}, использовано последний раз: {GREEN}{last}{CYAN}, тип торента: {GREEN}{category}{CYAN}, название торента: {GREEN}{name}{CYAN}, размер торента: {GREEN}{size}{CYAN}\n')
		except:
			print(f'{CYAN}[{RED}-{CYAN}] Unkown error ¯╲_(ツ)_/¯')
	elif shell == '5':
		res1 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes')
		print(f'{CYAN}[{RED}*{CYAN}] Your proxy, ser:\n' + '\n'.join(res1.text.split('\r\n')))
	elif shell == '6':
		phone = input(f'{CYAN}[{RED}*{CYAN}] Phone Number: {GREEN} ')
		try:
			page = requests.get('https://mirror.bullshit.agency/search_by_phone/'+phone)
			soup = BS(page.text, 'html.parser')
			classsell=soup.find(class_='media-heading')
			namesell= soup.find_all('h4')
			for classsell in namesell:
				print(f"{CYAN}[{RED}*{CYAN}] Name: {GREEN}", classsell.text)
			classtext = soup.find(class_='text-muted')
			nametext = soup.find_all('span')
			for classtext in nametext:
				print(f"{CYAN}[{RED}*{CYAN}] Address and data:{GREEN} ", classtext.text)
		except:
			print(f'{CYAN}[{RED}-{CYAN}] Unkown error ¯╲_(ツ)_/¯')
	elif shell == '7':
		query = input(f'{CYAN}[{RED}*{CYAN}] BSSID: {GREEN} ')
		try:
			response = requests.get("https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + query)
			data = response.json()
			status = data["result"]
			if status == 200:
				lat = data["data"]["lat"]
				lon = data["data"]["lon"]
				print(f'{CYAN}[{RED}*{CYAN}] Latinude: {GREEN}{lat}{CYAN}\n{CYAN}[{RED}*{CYAN}] Longitude: {GREEN}{lon}')
			else:
				errorCode = data["message"]
				errorMessage = data["desc"]
				print(f'{CYAN}[{RED}*{CYAN}] Error code: {GREEN}{errorCode}{CYAN}\n{CYAN}[{RED}*{CYAN}] Error message: {GREEN}{errorMessage}{CYAN}')
		except:
			print(f'{CYAN}[{RED}-{CYAN}] Пиши вверно! или ты лох')