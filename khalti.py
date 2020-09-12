import requests
import os
import configparser

config = configparser.ConfigParser()
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config.read(os.path.join(path, 'config.conf'))
email = config['config']['email']
password = config['config']['password']

def get_token():
    url = 'https://khalti.com/api/auth/login/'
    data = {'id':email,'password':password}
    resp = requests.post(url,data=data)
    headers = (resp.headers['Set-Cookie'])
    csrf = headers.split("; expires=")[0].replace('csrftoken=','')
    session_id = headers.split(" sessionid=")[1].split('; expires=')[0].replace(' sessionid=','')
    if resp.json()['idx']:
        return {'csrf_token':csrf,'session_id':session_id}

def very_latest_transaction():
    data = get_token()
    if data:
        url = 'https://khalti.com/api/transaction/?search=&service=&type=e476BL6jt9kgagEmsakyTL&status=&start_date=&end_date='
        headers = {'X-Security-CSRF-Token':data['csrf_token']}
        cookies= {'sessionid':data['session_id']}
        resp = requests.get(url,headers=headers,cookies=cookies).json()
        sender = (resp['records'][0]['transaction_params']['From']).split('(')[0]
        amount= str(resp['records'][0]['amount'])
        actual_amount = amount.replace(amount[-1],'').replace(amount[-1],'')
        remarks = (resp['records'][0]['remarks'])
        dict = {'sender':sender,'amount':actual_amount,'remarks':remarks}
        return dict
    

