from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(executable_path='/Users/shawn/Downloads/geckodriver')
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')


def not_now():
    not_now = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    not_now.click()

def dont_save():
    dont_save = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    dont_save.click()

class LogIn():
    def __init__(self, name, pw):
        self.name = name
        self.pw = pw

    def enter_name(self):
        enter_name = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        enter_name.click()
        enter_name.send_keys(self.name)

    def enter_pw(self):
        enter_pw = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        enter_pw.click()
        enter_pw.send_keys(self.pw)

    def enter(self):
        enter = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
        enter.click()


class User():
    def __init__(self, search):
        self.search = search


    def searchitem(self):
        searchitem = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        searchitem.click()
        searchitem.send_keys(self.search)
        clickitem = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span")
        clickitem.click()

    def followtags(self):
        n=0
        followtags = browser.find_element_by_xpath("/html/body/div[1]/section/main/header/div[2]/div[1]/button")

        followtags.click()
        n+=1
        sleep(5)

        while n<11:
            tagdictionary = {1:'/html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[1]/a', 2:'/html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[2]/a', 3:'/html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[3]/a', 4:'/html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[4]/a', 5:'/html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[5]/a' }
            findtag = browser.find_element_by_xpath(tagdictionary[3])
            followtags = browser.find_element_by_xpath("/html/body/div[1]/section/main/header/div[2]/div[1]/button")

            findtag.click()
            sleep(5)
            followtags.click()
            n+=1
            sleep(5)

    def clickphoto(self):
        clickthumbnail = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div")
        clickthumbnail.click()

    def likephoto(self):
        likebutton = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
        likebutton.click()

    def nextphoto(self):
        next = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")
        next.click()

    def nextnextphoto(self):
        nextnext = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
        nextnext.click()


myaccount=LogIn('autoart___', 'XXXXXXXXX')
myaccount.enter_name()
myaccount.enter_pw()
myaccount.enter()

sleep(3)

dont_save()
sleep(3)

not_now()
sleep(1)


inputElement = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
inputElement.send_keys("\n")

test = User('#porscheclub')
test.searchitem()
sleep(5)

likecount = 0
test.clickphoto()
sleep(5)
test.likephoto()
likecount += 1
sleep(1)
test.nextphoto()

while likecount < 195:
    sleep(3)
    test.likephoto()
    sleep(3)
    test.nextnextphoto()
    likecount += 1
    print(likecount)

browser.close()


