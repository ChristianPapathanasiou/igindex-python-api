import requests
import json

key = ""
username = ""
password = ""

class igservice:
	BASIC_HEADERS = None
	LOGGED_IN_HEADERS = None
	CST = None
	XS = None

	def __init__(self):
	
		self.BASIC_HEADERS = {
			'X-IG-API-KEY': key,
			'Content-Type': 'application/json', 
			'Accept': 'application/json; charset=UTF-8'
			}
		
		self.create_session()
	
	def _set_headers(self, response_headers, update_cst):
		if update_cst == True:
			self.CLIENT_TOKEN = response_headers['CST']
		try:
			self.SECURITY_TOKEN = response_headers['X-SECURITY-TOKEN']
		except:
			self.SECURITY_TOKEN = None
		self.LOGGED_IN_HEADERS = { 
			'X-IG-API-KEY': key,
			'X-SECURITY-TOKEN': self.SECURITY_TOKEN,
			'CST': self.CLIENT_TOKEN,
			'Content-Type': 'application/json',
			'Accept': 'application/json; charset=UTF-8' 
        }
        

       	 
	def create_session(self):
		params = { 
		'identifier': username,
		'password': password
		}
		response = requests.post("https://api.ig.com/gateway/deal"  + '/session', data=json.dumps(params), headers=self.BASIC_HEADERS)
		self._set_headers(response.headers,True)
		print response.text

	def search_markets(self,search_term):
		response = requests.get("https://api.ig.com/gateway/deal" + '/markets?searchTerm=%s' % search_term, headers=self.LOGGED_IN_HEADERS)
		data = response.text
		return json.loads(data)

	def fetch_client_sentiment_by_instrument(self,market_id):
		response = requests.get("https://api.ig.com/gateway/deal" + '/clientsentiment/%s' % market_id, headers=self.LOGGED_IN_HEADERS)
		data = response.text
		return(json.loads(data))
		
	def create_open_position(self, currency_code, direction, epic, expiry, force_open,guaranteed_stop, level, limit_distance, limit_level, order_type, quote_id, size, stop_distance, stop_level):
		params = {
			'currencyCode': currency_code,
			'direction': direction,
			'epic': epic,
			'expiry': expiry,
			'forceOpen': force_open,
			'guaranteedStop': guaranteed_stop,
			'level': level,
			'limitDistance': limit_distance,
			'limitLevel': limit_level,
			'orderType': order_type,
			'quoteId': quote_id,
			'size': size,
			'stopDistance': stop_distance,
			'stopLevel': stop_level
		}
		response = requests.post("https://api.ig.com/gateway/deal" + '/positions/otc', data=json.dumps(params), headers=self.LOGGED_IN_HEADERS)
		
		if response.status_code == 200:
			deal_reference = json.loads(response.text)['dealReference']
			return(deal_reference)
		else:
			return(response.text)

	def return_tokens(self):
		return(self.CLIENT_TOKEN,self.SECURITY_TOKEN)
    

	
	
	

