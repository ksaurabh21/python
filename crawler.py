#import urllib2
#seed_page = "http://www.google.com"
seed_page = "http://www.udacity.com/cs101x/index.html"
#seed_page = "http://cs101.udacity.com/urank/index.html"
#seed_page = "http://www.ge.com/"

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

#page = '<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Udacity</title></head><body><h1>Udacity</h1><p><b>Udacity</b> is a private institution of<a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".</p>   <p> It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>      </body></html>'

def get_next_target(s):
    start_link = s.find('<a href=')
    if(start_link==-1):
        return None, -1
    #print(start_link)
    start_quote = s.find('"http',start_link)
    #print(start_quote)
    end_quote = s.find('"',start_quote+1)
    url = s[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(page):
    while(True):
        url,end_quote=get_next_target(page)
        if url:
            print(url)
            page=page[end_quote:]
        else:
            break
            
def get_all_links(page):
    links= []
    while(True):
        url,end_quote=get_next_target(page)
        if url:
            links.append(url)
            page=page[end_quote:] #chopping off page before finding the next link
        else:
            break
    return links

# union takes as inputs two lists.
# It modifies the first input
# list to be the set union of the two
# lists.
def union(l1,l2):
    for elem in l2:
        if elem not in l1:
            l1.append(elem)


def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

#print_all_links(page_source)
#allLinks = get_all_links(page_source)
#print("*********print list***************")
#print(allLinks)

def compute_ranks(graph):
    d = 0.8 #damping factor
    numloops = 10 #number of timesteps. higher the number of timesteps, more accurate ranking you get
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0/npages #all pages have same rank in the begining

    for i in range(0,numloops):
        newranks = {}
        for page in graph:
            newrank = (1-d)/npages
            #sumofranks = 0
            for node in graph:
                if page in graph[node]: #what we need to do if a page has a link pointing to itself
                    newrank = newrank + (d*ranks[node])/len(graph[node])
            #newrank
            #
            #
            newranks[page] = newrank
        ranks = newranks
    return ranks

#lucky_search takes a single keyword and returns the highest ranking page for that keyword
def lucky_search(index, ranks, keyword):
    allpages = lookup(index, keyword) #get all pages that contain the keyword
    if not allpages:
        return None
    maxrank = 0
    bestpage = None
    for page in allpages: #go through all the pages to get highest ranking page
        if ranks[page]>maxrank:
            maxrank = ranks[page]
            bestpage = page
    return bestpage

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    print("tocrawl",tocrawl)
    print("crawled",crawled)

    while(tocrawl):
        
        link = tocrawl.pop()
        if link not in crawled:
            page_source = get_page(link)
            add_page_to_index(index,link,page_source)
            outlinks = get_all_links(page_source)
            union(tocrawl,outlinks)
            graph[link] = outlinks
            crawled.append(link)
        #print("tocrawl",tocrawl)
        #print("crawled",crawled)

    print("...finished crawling...")
    return index, graph

index, graph = crawl_web(seed_page)
for elem in index:
    print elem
    print index[elem]
    print "******************************"
