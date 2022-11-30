from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter:
    def __init__(self,username,password):
        
        #DİLLERİ ACTİVE ETMEYE YARAR ===>
        #self.browserProfile = webdriver.ChromeOptions()
        #self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages': 'en,en_US'})
        #self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        #     <====
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        
        
        self.username = username
        self.password = password
        
    def singIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(4)
        
        usernameInput = self.browser.find_element(By.NAME, 'text')
        usernameInput.send_keys(self.username)
        buttonclick = self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        buttonclick.click()
        time.sleep(3)
        
        passwordInput = self.browser.find_element(By.NAME, "password")
        passwordInput.send_keys(self.password)
        buttonclick = self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        buttonclick.click()
        time.sleep(5)
        
    def search(self,hashtag):
        searchInput = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        results = []
        
        list = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
        time.sleep(2)
        print("count :"+ str(len(list)))
        for i in list:
            results.append(i.text)
            
        loopCounter = 0
        # Scroll barını oynatmak için javascript kodu çalıştırır ======>
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
            
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1

            list = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
            time.sleep(2)
            print("count :"+ str(len(list)))
            for i in list:
                results.append(i.text)
            
        #list = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweet']/div[0]/div[0]/div[0]/div[1]/div[1]/div[1]/div[10]/div[0]")
        list = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
        time.sleep(3)
        print("count :"+ str(len(list)))
        
        for i in list:
            results.append(i.text)
            
        count = 1
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}--{item}\n")
                count +=1
            
        
        # count = 1
        # for item in results:
        #     print(f"{count}--{item}")
        #     count +=1
        #     print("************")
            
        
twitter = Twitter(username,password)
twitter.singIn()
twitter.search("python")