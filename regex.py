from bs4 import BeautifulSoup
import re
with open ('sample.html','r') as html_file:
    content=html_file.read()
    soup = BeautifulSoup(content,'lxml')

    
    print("Link for the Jquer website")
    print(soup.find_all(href=re.compile("jQuer")))
    print("Link for the react.js website")
    print(soup.find_all(href=re.compile("react")))
    print("Link for the WooCommerce website")
    print(soup.find_all(href=re.compile("WooCommerce")))
    print("Link for the Bootstrap website")
    print(soup.find_all(href=re.compile("Bootstrap")))
    print("Link for the Shopify website")
    print(soup.find_all(href=re.compile("Shopify")))
    print("Link for the Next.js website")
    print(soup.find_all(href=re.compile("Next.js")))
    print("Link for the Materialize CSS website")
    print(soup.find_all(href=re.compile("Materialize")))
    print("Link for the PHP website")
    print(soup.find_all(href=re.compile("php")))
    print("Link for the Python website")
    print(soup.find_all(href=re.compile("python")))
    print("Link for the Google Maps website")
    print(soup.find_all(href=re.compile("Google")))
     
