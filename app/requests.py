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
    """ Function that changes argument a list of form the api into 
        
        Args:
            source_list : alist of dictionaries 
        returns:
            source_results 
    """
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description') 
        url = source_item.get('url') 
        url_to_image = source_item.get("urlToImage")
        category = source_item.get("category") 

        if url_to_image:

            source_result = Sources(id, name, description, url, url_to_image, category)
            source_results.append(source_result)

    return source_results
     
# getting article information 
def get_article(category):

    """ function that get article information from the api """

    #getting the url
    article_url= article_base_url.format(category,api_key)
    
    with urllib.request.urlopen(article_url) as url:
        article_data = url.read()
        article_response = json.load(article_data)
  
    article_results = None

    if article_response['article']:       
        article_list = article_response['article']
        article_results = process_article(article_list)

    return article_results

def process_article(list_articles):
    """ a function that take in a list of dictionaries an processes them into objects 
      
       Arg:
         list_ariticle : a list of of dictionaries with informtion on the news
       returns:
          article_result : a list of article objects 
    """    
    article_results = []

    for list_article in list_articles :

        source_name = list_article.get('source.name')
        author = list_article.get('author')
        title = list_article.get('title')
        description = list_article.get('description')
        url_to_image = list_article.get('urlToImage')
        published_at = list_article.get('published_at')

        if url_to_image:
            article_object = Article(source_name, author, title, description, url_to_image, published_at)
            article_results.append(article_object) 
            
    return article_results




        
