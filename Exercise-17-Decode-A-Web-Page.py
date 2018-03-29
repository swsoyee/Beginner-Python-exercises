'''
Exercise 17: Decode A Web Page

This is the first 4-chili exercise of this blog! We’ll see what people think, 
and decide whether or not to continue with 4-chili exercises in the future.

Use the BeautifulSoup and requests Python packages to print out a list of all 
the article titles on the New York Times homepage.

'''
# Solution
import requests
from bs4 import BeautifulSoup

def get_html_content_in_text(url):
    """
    Grab all the content in webpage url and return it's content in text.
    
    Arguments:
    url -- a webpage url string.
    
    Returns:
    r.text -- the content of webpage in text.
    
    """
    r = requests.get(url)
    return r.text

def main():
    content = get_html_content_in_text('http://www.nytimes.com/')
    soup = BeautifulSoup(content, "html5lib")
    for element in soup.find_all(class_="story-heading"):
        if element.a:
            print(element.a.text.replace("\n", " ").strip())
        else: 
            print(element.contents[0].strip())
    
if __name__ == "__main__":
    main()

# Test Part - 2018-3-29
# Trump Lawyer Broached Idea of Pardons for 2 Top Ex-Aides
# Trump Aide Spoke in ’16 to Person Tied to Russia Intelligence
# Justice Dept. Opens Internal Investigation on Surveillance of Trump Campaign Official
# ‘Kiss Up, Kick Down’: Recalling Bolton’s Confirmation in 2005
# Veterans Affairs Chief Is Out, as Trump’s Shake-Up Continues
# The Trump Administration’s Major Departures
