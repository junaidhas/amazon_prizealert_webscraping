# amazon_prizealert_webscraping
An automated Amazon product prize alert app using BeautifulSoup web scraping library

-- Using the BeautifulSoup module, web scrape the Amazon product to find its current prize.
-- Need to add headers"User-Agent" and "Accept-Language"
-- U can find the header from https://myhttpheader.com/
-- I was checking an Asics running shoe, Its current price is 69$ CA, 
-- I cross-checked the shoe on camelcamelcamel.com website, 
--  this shoe usually costs 100-130$ in the last 16 months
-- Get an email using smtplib, whenever this shoe price is less than 80 $
-- We can automate this by running this program on the cloud, which will run this program every day,
-- and if the current price is less than our preferred buy prize we will get an email
