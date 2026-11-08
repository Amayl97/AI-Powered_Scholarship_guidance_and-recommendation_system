import requests
from bs4 import BeautifulSoup


# Function for extracting data from individual page
def extract_info(url):
   page_response = requests.get(url)

   html_response = page_response.text

   soup_for_page = BeautifulSoup(html_response, "html.parser")
   
   # h2 heading is the title of scholarship
   headings = soup_for_page.find_all("h2")
   
   # loop through all, but here in this page we have only 1 h2
   for heading in headings:
       print(heading.text)
   
   # now extract h3 headings
   headings_h3 = soup_for_page.find_all("h3")
   
   for heading_h3 in headings_h3:
       # Printed h3
       print(heading_h3.text)
       # get the ul next to each h3
       ul_data = heading_h3.find_next("ul")
       # get the li of each ul
       li_data = ul_data.find_all("li")
       # print the li
       for li in li_data:
           print(li.text)
   
       print("----------------------------------------------------------------------------")
   



def main():
    website_url = "https://scholarshipscorner.website/scholarships/"
    response = requests.get(website_url)
    
    print(response.status_code)
    html_data = response.text
    
    
    # For saving the html code into a file 
    # with open("page.html", "w", encoding="utf-8") as file:
    #     file.write(html_data)
    
    soup = BeautifulSoup(html_data, "html.parser")
    
    # extract all the links (a tag) from the page
    a_links = soup.find_all("a", class_="elementor-post__thumbnail__link")
    
    
    page_url_list = []
    for link in a_links:
        page_url = link.get("href")
        page_url_list.append(page_url)
       
    
    for page in page_url_list:
        extract_info(page)
        print("\n**************************************************************************\n")
   

if __name__ == "__main__":
    main()
