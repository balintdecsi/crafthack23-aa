import requests
from bs4 import BeautifulSoup


def request_url(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='feedbackcontent')
    return results


def get_page_number(URL):
    
    results = request_url(URL)
    
    if results.find_all("li")==[]:
        page_num = 1
    else:
        a=results.find_all("li")
        if str(a[-1])[-13].isdigit()==True:
            page_num = str(a[-1])[-13:-10]
        else: 
            if str(a[-1])[-12].isdigit()==True:
                page_num = str(a[-1])[-12:-10]
            else:
                page_num = str(a[-1])[-11:-10]
    return page_num 
    

def get_review_corpus(URL):
    
    review_corpus = ''
    
    if 'feedback' in URL:
        i = URL.index('/feedback')
        URL_long = URL[:i] + '/feedback/page-'

    else:
        URL_long = URL + '/feedback/page-'
    
    for page_num in range(1, int(get_page_number(URL))+1 ):
        URL_page = URL_long + str(page_num)
        results_page = request_url(URL_page)
        job_elements = results_page.find_all("div", class_="frame")
        
        for job_element in job_elements:
            location_element = job_element.find("p")
            x=location_element.text
            review_corpus = review_corpus + x + " "
    return review_corpus 


def get_user_name(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='profile')
    job_elements = results.find_all("h2", id="username_head")
    username_element = job_elements[0]  
    username = username_element.text.strip()
    return username 
    
