import requests
from bs4 import BeautifulSoup
import re



class OddballScraper ():
    
    def __init__(self):
        pass
    
    def print_jobs(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        html = requests.get("https://oddball.io/jobs/", headers=headers)
        doc = BeautifulSoup(html.text, 'html.parser')
        # print(doc)
        oddj = doc.select('.entry-content')[0].select('#oddball-jobs')[0]
        jobs = oddj.select('div')[0]
        print(jobs)
        
        job_list = []
        # for job in jobs:
        #     job = {
        #         'title': job.select("p")[0]("a")[0].attrs("href")
        #     }
        #     print(job['title'])
        #     job_list.append(job)

        
            



s1 = OddballScraper()

print(s1.print_jobs())
 


