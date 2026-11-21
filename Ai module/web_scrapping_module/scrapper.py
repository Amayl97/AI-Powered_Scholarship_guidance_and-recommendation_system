import os
import requests
from bs4 import BeautifulSoup
import json

field_mapping = {
    "country": ["host country", "country" ,"Host Country"],
    "host university": ["host university", "host universities"],
    "degree level": ["degree level"],
    "eligible countries": ["eligible countries"],
    "location": ["program location", "Program Location"],
    "duration": ["program duration"],
    "benefits": ["benefits of university", "benefits of", "benefits"],
    "Required Documents": ["required documents"],
    "eligibility": ["eligibility criteria", "Eligibility Criteria for University of Oxford Ertegun Scholarships  in UK"],
    "application process": ["documents", "apply", "how to apply for", "apply"],
    "deadline": ["program deadline", "application deadline for", "deadline"]
}


# Function for extracting data from individual page
def extract_info(url):

    scholarship = {}

    page_response = requests.get(url)
    page_response.raise_for_status()

    html_response = page_response.text
    soup_for_page = BeautifulSoup(html_response, "html.parser")

    # Extract scholarship title
    heading = soup_for_page.find("h2")

    if heading:
        scholarship["title"] = heading.get_text(strip=True).replace(":", "")

    # Extract h3 headings
    headings_h3 = soup_for_page.find_all("h3")

    for heading_h3 in headings_h3:

        # Extract heading
        heading = heading_h3.get_text(strip=True).lower().replace(":", "")

        # Check mapping
        for key, keywords in field_mapping.items():
           

           if any(phrase.lower() in heading for phrase in keywords):

                ul_data = heading_h3.find_next("ul")

                if ul_data:
                    li_data = ul_data.find_all("li")

                    values = []

                    for li in li_data:
                        values.append(li.get_text(strip=True))

                    scholarship[key] = values

                break

    # print(scholarship)

    return scholarship


def main():

    page_url_list = [
        "https://scholarshipscorner.website/university-of-oxford-ertegun-scholarships-uk/",
        "https://scholarshipscorner.website/noha-erasmus-mundus-scholarship/",
        "https://scholarshipscorner.website/berlin-school-of-economics-phd-program/",
        "https://scholarshipscorner.website/hainan-university-csc-scholarship/",
        "https://scholarshipscorner.website/netherlands-government-scholarship/",
        "https://scholarshipscorner.website/commonwealth-shared-scholarships/"
    ]

    all_scholarships = []

    for page in page_url_list:
        data = extract_info(page)
        all_scholarships.append(data)
    file_path = "/Users/amayl/Desktop/Final_Year_Project/Scholarship_guidance_recommendation_FYP/Ai module/web_scrapping_module/data/scholarships.json"

    with open(file_path ,"w", encoding="utf-8") as file:
        json.dump(all_scholarships, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()


