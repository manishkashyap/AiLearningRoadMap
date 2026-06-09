""" 
    Act as an expert software engineer specializing in web scraping and automation. 

    Build a web crawler designed to extract data from the following websites:
    1. https://docs.webengage.com/
    2. https://webengage.com/blog/
    3. https://knowledgebase.webengage.com/docs/preface
    4. https://webengage.com/resource/ebook/
    5. https://webengage.com/resource/glossary/


    ### Execution Rules
    The crawler must strictly adhere to the following rules to ensure ethical, polite, and uninterrupted execution:
    1. Respect Robots.txt: Parse the robots.txt file for each domain. Do not crawl any paths marked as "Disallow".
    2. Rate Limiting: Implement a mandatory crawl delay of [Insert seconds, e.g., 2] seconds between sequential requests to avoid overloading the server.
    3. User-Agent Identification: Set a custom User-Agent header that clearly identifies this bot (e.g., "CustomDataBot/1.0 (+http://yourdomain.com)").
    4. Loop and Depth Control: Set a maximum crawl depth of [Insert number, e.g., 3] levels to prevent infinite loops.
    5. Error Handling: Monitor HTTP status codes. If a '429 Too Many Requests' or '503 Service Unavailable' is encountered, implement an exponential backoff strategy (pause and slow down).
    6. Data Target: Extract the following specific fields: [Insert fields, e.g., Page Title, Main Article Text, Publication Date].
    7. Output Format: Save the successfully scraped data cleanly into an MD file.

    Please provide the complete, commented code and step-by-step instructions on how to install dependencies and run the script.

"""