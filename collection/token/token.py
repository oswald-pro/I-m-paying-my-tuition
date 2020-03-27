import httplib, urllib, base64
api_user = "201"
api_key = "79f55c2fdd164d0cafa5530a7e8a9384"
api_user_and_key  = api_user+':'+api_key
encoded = base64.b64encode(api_user_and_key)
headers = {
    # Request headers
    'Authorization': 'Basic '+encoded,
    'Ocp-Apim-Subscription-Key': 'f262afa7a68a4acfac4f60a93cf0b017',
}
params = urllib.urlencode({
})
try:
    conn = httplib.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/collection/token/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))