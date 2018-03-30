'''
Exercise 19: Decode A Web Page Two

Using the requests and BeautifulSoup Python libraries, print to the 
screen the full text of the article on this website: 

http://content.time.com/time/magazine/article/0,9171,2005869-1,00.html

The article is long, so it is split up between 2 pages. Your task
is to print out the text to the screen so that you can read the full
article without having to click any buttons.

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
    content = get_html_content_in_text('http://content.time.com/time/magazine/article/0,9171,2005869-1,00.html')
    soup = BeautifulSoup(content, "html5lib")
    print(soup.select('div > p'))
    next_page = soup.find_all(class_='next')[0].get('href')
    content_next_page = get_html_content_in_text('http://content.time.com/' + next_page)
    soup_next = BeautifulSoup(content_next_page, "html5lib")
    print(soup_next.select('div > p'))
        
    
if __name__ == "__main__":
    main()
    
# Test Part
# ------------------
# [<p><b>Correction Appended: July 22, 2010</b></p>, <p>All politics may be local, but apparently not enough journalism is. As newspapers keep cutting back on staff and printing skimpier editions, journalists, entrepreneurs and ordinary citizens have responded by creating websites to cover the local news they feel is going underreported — like the serious windstorm that hit Tracy Record's Seattle neighborhood in 2006. "Every day we break stories," says Record, the editor and primary reporter for West Seattle Blog, a site she and her husband created as an information hub after the storm. "In the past hour, I learned a major parks project is being delayed because of drainage trouble and just broke that on our site." She also covers car crashes, crime, council meetings, bake sales and walkathons for the 70,000 or so Seattle residents who live west of the Duwamish River. "If they were able to get the local news they needed elsewhere, we wouldn't have wound up doing this," says Record. </p>, <p><i>Hyperlocal</i> has become a buzzword as familiar to news junkies as <i>eat local</i> is to foodies. The idea is to get residents involved in the reporting not just by sending in tips but by writing content about important local issues such as school boards and transportation. In professional newsrooms, "we spend too much time on craft and not enough time on community," says Michele McLellan, a fellow at the Reynolds Journalism Institute at the University of Missouri who spent the past year studying nearly 70 of the best hyperlocal sites. "Many of the new sites, even if they don't have the most polished reports, are flipping that: community first." </p>, <p></p>, <p>McLellan, who will present her findings in September at the Block by Block: Community News Summit 2010 in Chicago, concluded that 1 in 10 hyperlocal sites is producing "good" content, some good enough to give traditional journalism a run for its money — sometimes literally. After years of relying on donation drives to keep going, Record's West Seattle Blog made six figures in revenue last year before taxes; the same is expected for 2010. </p>, <p>
# 
# Sensing the potential of niche news, the Knight Foundation, a nonprofit journalism organization, has given out roughly $20 million in grants since 2006 to help nurture the most promising sites. Last August, msnbc.com bought EveryBlock, which posts public records and news searchable by ZIP code in 16 cities. And in March, AOL announced plans to invest up to $50 million in local initiatives like Patch, which provides community-specific news in 65 towns and expects to service hundreds more by the end of this year.</p>, <p>Megasites like EveryBlock are also pushing the boundaries of hyperlocal. EveryBlock runs individual community sites from its headquarters in Chicago and populates them mostly with publicly available data such as crime reports, building permits and restaurant inspections. "Many journalists would say good journalism is about good storytelling," says EveryBlock founder and former WashingtonPost.com editor Adrian Holovaty. "As much as I love a compelling story, I think good journalism can also be about organizing information in intelligent ways and giving people tools that let them help each other." </p>, <p></p>, <p></p>, <p> </p>, <p></p>, <p><span class="icon twitter"></span> Follow <a href="http://twitter.com/TIME/" target="_blank">@TIME</a></p>]
# [<p><span class="page">(2 of 2)</span><br/></p>, <p><span style="font-weight: bold">Databases vs. Shoe Leather</span><br/>
# Most hyperlocal sites don't have the budget for flashy graphics or searchable databases. Their content comes from observant neighbors (and local gadflies) who care about both large and small goings-on around town. Hyperlocal sites also frequently publish upbeat accounts of parades and high school sports, as well as information on which local vendors sell the best produce. Recent headlines on Record's site noted a "mega-low" tide and an upcoming garden tour.</p>, <p>Some traditional news organizations, in addition to partnering with hyperlocal sites and helping train their contributors, are creating their own local outlets. In 2009 the New York <i>Times</i> launched the Local, a project that involved two news sites, serving northern New Jersey and parts of Brooklyn, which were produced by residents and student journalists with oversight from <i>Times</i> staff. (The paper handed off its Jersey coverage to another hyperlocal site at the end of June; the Brooklyn site is now run by the City University of New York in partnership with the <i>Times</i>.) Next up for the <i>Times</i> is a collaboration with New York University's Arthur L. Carter Journalism Institute to cover Manhattan's East Village. "Our goal is to support good journalism, be good partners to two of the leading journalism graduate schools in the country, and share information, ideas, resources and initiatives, with the goal of figuring out new relationships that will allow news organizations to extend their reach," says Mary Ann Giordano, the <i>Times</i>'s deputy Metro editor, who oversees collaborative and hyper-local coverage. "The bonus is we also get to serve these two communities."</p>, <p></p>, <p>Record spent 30 years as a journalist, but it's her work on the West Seattle Blog — where she oversees (and pays) a handful of freelance contributors — that is earning her awards and teaching gigs. For two years, she has been teaching at the Poynter Institute, a nonprofit journalism training center in St. Petersburg, Fla. In May she was one of a dozen so-called digital entrepreneurs invited to participate in a News Entrepreneur Boot Camp at the University of Southern California's Annenberg School for Communication and Journalism, where she coached others on sustainable business models, revenue strategies and social-networking tactics</p>, <p>But on a day-to-day basis, Record sits in her living room reinventing the role of an old-school newspaper editor. In June, when a "For sale" sign went up on a prominent, long-vacant building owned by the federal government, a devoted reader sent Record a quick eâmail with an attached photo. Record then went to work reporting the story. "Not Woodward-Bernstein stuff," she says. "But this apartment building is now long abandoned, overgrown, boarded up, graffiti-vandalized, and thousands of people drive by it every week. They want to know what's happening with it. So this is a story, and we will continue to follow it."</p>, <p><i>The original version of this story said MSNBC bought EveryBlock. EveryBlock was bought by msnbc.com, a separate company from MSNBC.</i></p>, <p><i>This story appeared in the August 2, 2010 issue of TIME Magazine.</i></p>, <p> </p>, <p></p>, <p> </p>, <p></p>, <p><span class="icon twitter"></span> Follow <a href="http://twitter.com/TIME/" target="_blank">@TIME</a></p>]
