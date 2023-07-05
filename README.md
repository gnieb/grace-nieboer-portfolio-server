# Grace Nieboer Portfolio Server
## About
this pairs with the front end portfolio repo [HERE]()

## Web scraper Notes

how to bypass 403 forbidden - 
1. inspect the page
2. Network Tab -> refresh the page -> double click an item call with the same domain as the website -> headers tab --> scroll down to User Agent info and copy to clipboard -> create headers object like so:

headers = {
    'user-agent':'copied user-agent header from dev tools'
}