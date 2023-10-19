import requests

headers = {
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'X-IG-WWW-Claim': '0',
    'sec-ch-ua-platform-version': '"8.0.0"',
    'X-Requested-With': 'XMLHttpRequest',
    'dpr': '1',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.72", "Google Chrome";v="118.0.5993.72", "Not=A?Brand";v="99.0.0.0"',
    'X-CSRFToken': 'tiYjyVQONwHONB0FsKKUSi74SfdRxIFL',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'X-IG-App-ID': '936619743392459',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua-mobile': '?0',
    'X-Instagram-AJAX': '1009345740',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'viewport-width': '811',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'https://www.instagram.com/',
    'X-ASBD-ID': '129477',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1697714235:AeFQACleu5LP0mLbrfZfuy7mXd2xwDN/WLfQA0DC8tEQd+1hlSoR4XgP7DNxVf5JD1reApKWv8t8P39ExTQ4bh2H39JTSFR0/+LPIVh2n4UC9bXZAwoGWXA0jrzf1WdhZPPoFT8MSVGoOaOSzw==',
    'optIntoOneTap': 'false',
    'queryParams': '{"oneTapUsers":"[\\"60482218657\\"]"}',
    'trustedDeviceRecords': '{}',
    'username': 'xyraacode',
}

response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
