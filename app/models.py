class Sources:  
    """ class that stores the source infomation """
   
    # sources_list=[] not required
  
    def __init__(self, id, name, description, url, category ):
        """ source infomation """
        self.id = id
        self.name = name 
        self.description = description
        self.url = url 
        self.category = category

        
         

class Article:
    """ class that stores information of the article """
    
    # article_list = [] bnot needed arent saving any infomation there.

    def __init___(self,source_name,author, title, description,published_at):
        """ article infomation """
        self.source_name = source_name
        self.author = author
        self.title = title 
        self.description = description 
        self.published_at = published_at