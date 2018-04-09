# needs configuration  to call infomation from the api. stores those functions here
 # also create local varibales of the keys and makes them global
import urllib.request,json
from models import Sources,Article

# getting the api key
api_key = None

# gettin the base urls
source_base_url = None #app.config[NEWS_S_BASE_URL]
article_base_url = None #app.config[NEWS_A_BASE_URL]

def config_requests(app):
    global api_key, source_base_url, article_base_url
    api_key = app.config['NEWS_API_KEY']
    source_base_url = app.config['NEWS_S_BASE_URL']
    article_base_url = app.config['NEWS_A_BASE_URL']

# getting the sources
def get_sources():
    """ Function that gets all the soures """
    get_sources_url = source_base_url.format(api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        source_data = url.read()
        source_response = json.load(source_data)

        source_results = None

        if source_response['source']:
             source_results_list = source_response['source']
             source_results = process_results(source_results_list)
    
    return source_results
    
def process_results(source_list):
    """ Function that map repose form the api into th model """
    source_results = []

    for source_item in source_list:
        id = source_item.id
        name = source_item.name
        description = source_item.description 
        url = source_item.description 
        url_to_image = source_item.urlToImage
        category = source_item.category 

        if url_to_image:

            source_result = Sources(id, name, description, url, url_to_image, category)
            source_results.append(source_result)

    return source_results
     
        