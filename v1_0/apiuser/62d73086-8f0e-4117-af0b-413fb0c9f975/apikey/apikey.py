import httplib, urllib, base64, uuid,json
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'f262afa7a68a4acfac4f60a93cf0b017'
}
params = urllib.urlencode({
})
body = json.dumps({
  "providerCallbackHost": <your application domain> })
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/v1_0/apiuser/62d73086-8f0e-4117-af0b-413fb0c9f975/apikey?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))