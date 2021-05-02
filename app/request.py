import urllib.request,json
from .models import Quote

# Getting quotes url
quote_url = None

def configure_request(app):
    global quote_url
    quote_url = app.config['QUOTES_URL']
    
    
def get_quotes():
  '''
  Function that gets the json response to our url request
  '''
  with urllib.request.urlopen(quote_url) as url:
    get_quote_data=url.read()
    quote_response=json.loads(get_quote_data)

    quote_results={}

    if quote_response['quote']:
      quote_results['id']=quote_response['id']
      quote_results['author']=quote_response['author']
      quote_results['quote']=quote_response['quote']

    return quote_results    