import requests 
import bs4 
import time 
import lxml 

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

site1 = ('https://www.ncbi.nlm.nih.gov/pubmed/23454191')
site2 = ('https://www.ncbi.nlm.nih.gov/pubmed/24956890')
site3 = ('https://www.ncbi.nlm.nih.gov/pubmed/27898007')
site4 = ('https://www.ncbi.nlm.nih.gov/pubmed/29467715')
site5 = ('https://www.ncbi.nlm.nih.gov/pubmed/25092271')
site6 = ('https://www.ncbi.nlm.nih.gov/pubmed/29462606') 
site7 = ('https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5482128')
site8 = ('https://www.ncbi.nlm.nih.gov/pubmed/29452253')
site9 = ('https://www.ncbi.nlm.nih.gov/pubmed/21836089')
site10 =('https://www.ncbi.nlm.nih.gov/pubmed/22910893')

req1 = requests.get (site1, headers=hdr)
req2 = requests.get (site2, headers=hdr)
req3 = requests.get (site3, headers=hdr)
req4 = requests.get (site4, headers=hdr)
req5 = requests.get (site5, headers=hdr)
req6= requests.get (site6, headers=hdr)
req7 = requests.get (site7, headers=hdr)
req8 = requests.get (site8, headers=hdr)
req9 = requests.get (site9, headers=hdr)
req10 = requests.get (site10, headers=hdr, timeout=5)

output1 = bs4.BeautifulSoup (req1.text,'lxml')
output2 = bs4.BeautifulSoup (req2.text,'lxml')
output3 = bs4.BeautifulSoup (req3.text,'lxml')
output4 = bs4.BeautifulSoup (req4.text,'lxml')
output5 = bs4.BeautifulSoup (req5.text,'lxml')
output6 = bs4.BeautifulSoup (req6.text,'lxml')
output7 = bs4.BeautifulSoup (req7.text,'lxml')
output8 = bs4.BeautifulSoup (req8.text,'lxml')
output9 = bs4.BeautifulSoup (req9.text,'lxml')
output10 = bs4.BeautifulSoup (req10.text,'lxml')

print(output1.dd)
print(output2.dd)
print(output3.dd)
print(output4.dd)
print(output5.dd)
print(output6.dd)
print(output7.dd)
print(output8.dd)
print(output9.dd)
print(output10.dd)



