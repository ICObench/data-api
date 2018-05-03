import hmac
import json
import hashlib
import base64
import urllib2

publicKey = ""
privateKey = ""

apiUrl = 'https://icobench.com/api/v1/'

data = {'search': 'DMarket'}

hash = hmac.new(privateKey, '', hashlib.sha384)

dataJSON = json.dumps(data)
hash.update(dataJSON)
sign = hash.digest()
sign = base64.b64encode(sign)

request_headers = {
'Accept': 'application/json',
'Content-Type': 'application/json',
'X-ICObench-Key': publicKey,
'X-ICObench-Sig': sign
}

print apiUrl + "icos/all"

request = urllib2.Request(apiUrl + "icos/all", data=dataJSON, headers=request_headers)
contents = urllib2.urlopen(request).read()
print contents
