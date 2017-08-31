# igindex-python-api

C. Papathanasiou 2015

A framework class for the IG Index API. 

Based on:
<br>
https://github.com/lewisbarber/ig-markets-rest-api-python-library/blob/master/ig_service.py

I couldn't get that one to work as relies heavily on the pandas library which is a nightmare to compile on MacOSX.

Refactored code, created barebones version for what I wanted to do (obtain sentiment, open position, search markets). 

Can easily be extended based on official IG Index API spec available here:
<br>
http://labs.ig.com/rest-trading-api-guide

<b>
Usage
</b>

```python
Christian-Papathanasious-iMac:igindex-library chris$ python
>>> from igindex import igservice
>>> c = igservice()
{"accountType":"SPREADBET","accountInfo":{"balance":0.0,"deposit":0.0,"profitLoss":0.0,"available":0.0},"currencyIsoCode":"GBP","currencySymbol":"ÂŁ","currentAccountId":"****","lightstreamerEndpoint":"https://apd.marketdatasystems.com","accounts":[{"accountId":"*****","accountName":"Spread bet","preferred":true,"accountType":"SPREADBET"},{"accountId":"***","accountName":"Stockbroking","preferred":false,"accountType":"PHYSICAL"}],"clientId":"******","timezoneOffset":0,"hasActiveDemoAccounts":true,"hasActiveLiveAccounts":true,"trailingStopsEnabled":false,"reroutingEnvironment":null,"dealingEnabled":true}
```

Then to e.g, search markets:

```python
>>> gold = c.search_markets("Gold")
>>> gold["markets"][0]
{u'instrumentName': u'Spot Gold', u'updateTime': u'15:55:40', u'streamingPricesAvailable': True, u'offer': 1290.55, u'bid': 1290.05, u'expiry': u'DFB', u'high': 1291.53, u'marketStatus': u'TRADEABLE', u'delayTime': 0, u'low': 1272.17, u'percentageChange': 0.7, u'epic': u'CS.D.USCGC.TODAY.IP', u'netChange': 8.92, u'instrumentType': u'CURRENCIES', u'scalingFactor': 1}
```
