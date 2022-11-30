from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
    
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        # self.browser.get("https://www.instagram.com/patika.dev")
        time.sleep(3)
        self.browser.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(2)
        dialog = self.browser.find_element(By.CSS_SELECTOR,'div[role=dialog]')
        followerCount = len(dialog.find_elements(By.CSS_SELECTOR,"li"))
        
        print(f"first count: {followerCount}")
        
        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            
            newCount = len(dialog.find_elements(By.CSS_SELECTOR,"li"))
            
            if newCount != followerCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break
        
        followers = dialog.find_elements(By.CSS_SELECTOR,"li")
        followerList = []
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            followerList.append(link)
            
        with open("followers.txt","w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
    
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton = []
        followButton = self.browser.find_elements(By.TAG_NAME,"button")
        if followButton[1].text == "Follow":
            followButton[1].click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin")
        
    def unFollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        
        followButton = []
        followButton = self.browser.find_elements(By.TAG_NAME,"button")
        if followButton[1].text != "Follow":
            followButton[1].click()
            time.sleep(2)
            unbutton = self.browser.find_element(By.XPATH,'//button[text()="Unfollow"]')
            unbutton.click()
            #self.browser.find_element(By.XPATH,'//*[@id="mount_0_0_k2"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click

        else:
            print("Zaten Takip Etmiyorsunuz")
            
instgram = Instagram(username,password)
instgram.signIn()
#instgram.getFollowers()
#instgram.followUser('kod.efendi')
#instgram.unFollowUser('kod.efendi')

list = ['miakhalifa','whitegirlpoliticking']
for user in list:
    instgram.unFollowUser(user)
    time.sleep(3)

