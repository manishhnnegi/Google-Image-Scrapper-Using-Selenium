from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from functions.creatfilept import *
from functions.folder_inside import *

def find_url(driver_path, query, search_count):
    try:
        executable_path= driver_path
        driver = webdriver.Chrome(executable_path)
        url = "https://www.google.com/search?q={q}&tbm=isch&sxsrf=APq-WBtKmGmTjnSU_ElDnDgOksqd9za5vA%3A1650816222935&source=hp&biw=1920&bih=969&ei=3nRlYtazN6y9hwOOlpLoBQ&iflsig=AHkkrS4AAAAAYmWC7rWDFS8B8k9HHGIg2K57J-3MjD7E&ved=0ahUKEwjWmrnUia33AhWs3mEKHQ6LBF0Q4dUDCAc&oq=narendra+modi&gs_lcp=CgNpbWcQDDIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQMyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwE6CggjEO8DEOoCECc6BwgjEO8DECc6CAgAELEDEIMBOgQIABADUJsMWP_eAWCQ7wFoEXAAeACAAbACiAGUGZIBBzAuNC43LjOYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img"

        driver.get(url.format(q=query))

        t = set()
        img_count = len(t)
        start = 0
        while img_count <= search_count:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            driver.implicitly_wait(10)
            f = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            end = len(f)
            max_count = len(f[start:end])
            if search_count < max_count:
                for i in f:
                    i.click()
                    time.sleep(1)

                    d = driver.find_elements(By.XPATH, '//img[@class="n3VNCb"]')
                    for j in d:
                        if j.get_attribute('src') and 'http' in j.get_attribute('src'):
                            p = j.get_attribute('src')
                            print("src")
                            t.add(p)
                            img_count = len(t)
                    if img_count == search_count:
                        break
                print("url links are fetched successfully now wait for downloding")
                return t
            else:
                print("image count out of range searching for more ....urls")

            #start = max_count


    except Exception as e:
        print("error is due to ___",e)

def search_and_downlode(driver_path, search_count, query):
    folder_nm = 'myimage'
    keyword = query
    inside_folder = query+"s"
    tp = find_url(driver_path, query, search_count)
    for i in range(search_count):
        try:
            url1 = tp.pop()

            #driver.get(url)
            image_content = requests.get(url1).content
            time.sleep(10)
            print("image dowloded")
        except Exception as e:
            print(f"ERROR - Could not download {url1} - {e}")

        try:
            folderIn(folder_nm, inside_folder)
            file = autofile_path(keyword, inside_folder, folder_nm)
            h = open(file, 'wb')
            h.write(image_content)
            h.close()
            print("image downloded and saved")
        except Exception as e:
            print(f"ERROR - Could not save {url1} - {e}")







driver_path = 'E:\IMZ\chromedriver.exe'
query ="himalayas"
search_count = 2
search_and_downlode(driver_path, search_count, query)