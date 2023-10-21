import feedparser

def get_rss_feed(url):
    feed = feedparser.parse(url)
    return feed

def get_guids(feed):
    guids = []
    for entry in feed.entries:
        guids.append(entry.guid)
    return guids

def main():
    feed_url = 'https://anchor.fm/s/1b6c6edc/podcast/rss'
    feed = get_rss_feed(feed_url)
    guids = get_guids(feed)

  # Print GUIDs
    strings=guids
    unique_strings = set(guids)

# Iterate over the set to find duplicates
    for string in unique_strings:
  # Check if the string appears more than once in the array
        if strings.count(string) > 1:
    # Print the string
            print(string)
    
   # for guid in guids:
    #    print(guid)

if __name__ == '__main__':
    main()