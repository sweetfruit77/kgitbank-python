from selenium import webdriver as wd
from tqdm import tqdm_notebook
import time
import sys

driver = wd.PhantomJS('./crawling/data/phantomjs')
filters = {
    'hour': 'EgQIARAB', # 지난 한시간
    'today': 'EgQIAhAB', # 오늘
    'week': 'EgQIAxAB', # 이번주
    'month': 'EgQIBBAB', #이번달
    'year': 'EgQIBRAB' #올해
}
word = 'BTS'
url = 'https://www.youtube.com/results?search_query={word}&sp={date}'.format(word=word, date=filters['today'])
driver.get(url)
time.sleep(3)

def getVideoElement():
    return driver.find_elements_by_tag_name('ytd-video-renderer')

def getVideoCount():
    return len(getVideoElement())
    
print(getVideoCount())
driver.save_screenshot('./crawling/data/sceern001.png')

driver.close()
driver.quit()
sys.exit()