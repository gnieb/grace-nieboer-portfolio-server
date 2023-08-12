# JobWave Server
[Front-End Application Here](https://github.com/gnieb/jobwave)
## About
This application was originally developed to help me get a job at a company I REALLY wanted to work for, but they didn't have the jobs posted that fit my qualifications. 
**Enter JobWave.**

### Built with
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 
* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
* ![Beautiful Soup](https://img.shields.io/badge/beautiful_soup-%23121011.svg?style=for-the-badge&logo=data:python/svg?&color=ff69b4)

## Features Completed
- postgres database established
- GUI configured wuth DBeaver
- Job and Encouraging quote models/tables built
- 


## Features in progress
- RESTful API 
- Web Scraper to pull job positions for 'Software Engineer' from select company websites
- Web Hook to send an email alert 
- Jobwave database needed to be deployed or hosted locally

## Web scraper Notes

how to bypass 403 forbidden - 
1. inspect the page
2. Network Tab -> refresh the page -> double click an item call with the same domain as the website -> headers tab --> scroll down to User Agent info and copy to clipboard -> create headers object like so:

headers = {
    'user-agent':'copied user-agent header from dev tools'
}


