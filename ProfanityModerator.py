import urllib.parse, http.client, json

headers = {
    'Ocp-Apim-subscription-Key':'[YOUR_KEY]',
    'Content-Type':'text/plain'
}

params = urllib.parse.urlencode({
    'PII':True
})

body = 'Crap! I just bumped my toe in the corner of this stupid chair, that chair is stupid. That is a really stupid chair. I hate the stupid chair. That chair is a fucking pussy.'

service_url = '[YOUR_SERVICES_LOCATION].api.cognitive.microsoft.com'

endpoint = '/contentmoderator/moderate/v1.0/ProcessText/Screen?%s' % params

try:
    conn = http.client.HTTPSConnection(service_url)
    conn.request('POST', endpoint, body, headers)
    response = conn.getresponse()
    jsonData = response.read()
    text_data = json.loads(jsonData)
    print(json.dumps(text_data, indent=2))
    conn.close()
except Exception as ex:
    print(ex)


moderatedText = text_data['OriginalText']

for term in text_data['Terms']:
    old_text = moderatedText[term['Index']:term['Index']+len(term['Term'])]
    new_text = '*' * len(old_text)
    moderatedText = moderatedText.replace(old_text, new_text)
    
print(moderatedText)