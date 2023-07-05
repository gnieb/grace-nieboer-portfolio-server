# Grace Nieboer Portfolio Server
## About
This application was originally developed to help me get a job at a company I REALLY wanted to work for, but they didn't have the jobs posted that fit my qualifications. 
**Enter JobWave.**


## Web scraper Notes

how to bypass 403 forbidden - 
1. inspect the page
2. Network Tab -> refresh the page -> double click an item call with the same domain as the website -> headers tab --> scroll down to User Agent info and copy to clipboard -> create headers object like so:

headers = {
    'user-agent':'copied user-agent header from dev tools'
}