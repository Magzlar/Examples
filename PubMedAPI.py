# Pull information from publications in PubMed database using API e.g. request abstracts and results section from publications that meet certain search criteria i.e Cannabidiol in pain 

from pymed import PubMed
import pandas as pd 


pubmed = PubMed(tool="PubMedSearcher", email="example@example.co.uk")

# place search term in search_term variable
search_term = "cannabidiol in stroke"
results = pubmed.query(search_term, max_results=1000)
articleList = []
articleInfo = []

for article in results:
# Print the type of object 
# convert to a dictionary to use index features 
    articleDict = article.toDict()
    articleList.append(articleDict)

# Generate dict which to hold all article details 
for article in articleList:
    pubmedId = article['pubmed_id'].partition('\n')[0]
    # Append article info to dictionary 
    articleInfo.append({'pubmed_id':pubmedId,
                       'title':article['title'],
                       'keywords':article['keywords'],
                       'journal':article['journal'],
                       'doi':article['doi'],
                       'publication_date':article['publication_date'], 
                       'authors':article['authors']})

# Generate pd data frame to access and manipulate data 
articlesPD = pd.DataFrame.from_dict(articleInfo)
df = pd.DataFrame(articlesPD)

#convert to excel file to use within other programmes

df.to_csv (r'C:\Users\USERNAME\Documents\RIC lab_name scraper\CBDStrokeDataMeta1.csv', index = None)
