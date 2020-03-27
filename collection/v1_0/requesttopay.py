import httplib, urllib, base64, uuid,json
token = <replace with token>
reference_id = str(uuid.uuid4())
headers = {
    # Request headersi
    'Authorization': 'Bearer '+token,
    #'X-Callback-Url': <replace with own http://myapp.com/momoapi/callback>,
    'X-Reference-Id': refrence_id,
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'f262afa7a68a4acfac4f60a93cf0b017>',
}
params = urllib.urlencode({})
body = json.dumps({
  "amount": "5000",
  "currency": "XAF",
  "externalId": "12345",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": "0780123456"
  },
  "payerMessage": "test message",
  "payeeNote": "test note"
})
try:
    conn = httplib.HTTPSConnection('andbox.momodeveloper.mtn.com')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))