from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys


path="chromedriver"

browser = webdriver.Chrome(executable_path=path)

kitap_adi=input("kitap adı giriniz: ")
yayin_evi=input("yayın evi giriniz: ")
def bkm_kitap():
    browser.get("https://www.google.com/")

    bkm_kitap_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    bkm_kitap_veri_girisi.send_keys(kitap_adi+ " "+ yayin_evi+ " "+" site:bkmkitap.com")
    time.sleep(2)

    bkm_kitap_veri_girisi.send_keys(Keys.ENTER)
  
    time.sleep(2)

    bkm_kitap_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div/div[1]/a/h3")
    bkm_kitap_tikla.click()

    bkm_kitap_sayfa = browser.page_source
    bkm_kitap_soup = BeautifulSoup(bkm_kitap_sayfa, "lxml")

    bkm_kitap_bilgiler = bkm_kitap_soup.find("div",attrs={"id":"productInfo"})

    bkm_kitap_adi = bkm_kitap_bilgiler.find("h1").text
    bkm_kitap_yayin_evi = bkm_kitap_bilgiler.find("a").text.strip()

    bkm_kitap_yazar_adi = bkm_kitap_bilgiler.find("a",attrs={"id":"productModelText"}).text.strip()

    bkm_kitap_fiyat = bkm_kitap_soup.find("span",attrs={"class":"product-price"}).text

    print("BKM KİTAP = "+ bkm_kitap_adi+ " , "+ bkm_kitap_yayin_evi+" , "+bkm_kitap_yazar_adi+" , "+bkm_kitap_fiyat)


    
def kitapyurdu():
    browser.get("https://www.google.com/")

    kitapyurdu_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    kitapyurdu_veri_girisi.send_keys(kitap_adi+ " "+ yayin_evi+ " "+" site:kitapyurdu.com")
    time.sleep(2)

    kitapyurdu_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    kitapyurdu_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div/div[1]/a/h3")
    kitapyurdu_tikla.click()

    kitapyurdu_sayfa = browser.page_source
    kitapyurdu_soup = BeautifulSoup(kitapyurdu_sayfa, "lxml")

    kitapyurdu_kitap_adi = kitapyurdu_soup.find("h1",attrs={"class":"pr_header__heading"}).text
    kitapyurdu_yazar_adi = kitapyurdu_soup.find("a",attrs={"class":"pr_producers__link"}).text.strip()
    kitapyurdu_yayin_evi = kitapyurdu_soup.find("div",attrs={"class":"pr_producers__publisher"}).text.strip()
    kitapyurdu_fiyat = kitapyurdu_soup.find("div",attrs={"class":"price__item"}).text.strip()


    print("KİTAP YURDU = "+ kitapyurdu_kitap_adi+" , "+kitapyurdu_yazar_adi+" , "+kitapyurdu_yayin_evi+" , "+kitapyurdu_fiyat)

def dr_kitap():
    browser.get("https://www.google.com/")

    dr_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    dr_veri_girisi.send_keys(kitap_adi+ " "+ yayin_evi+ " "+" site:dr.com.tr")
    time.sleep(2)

    dr_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    dr_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div/div[1]/a/h3")
    dr_tikla.click()

    dr_sayfa = browser.page_source

    dr_soup = BeautifulSoup(dr_sayfa, "lxml")
    
    dr_yazar_adi = dr_soup.find("span",attrs={"class":"name"}).text
    dr_yayin_evi = dr_soup.find("h2").text
    dr_kitap_adi  =dr_soup.find("h1",attrs={"class":"product-name"}).text.strip()
    dr_fiyat = dr_soup.find("span",attrs={"id":"salePrice"}).text

    print("DR KİTAP  = "+ dr_kitap_adi+" , "+dr_yayin_evi+" , "+dr_yazar_adi+" , "+dr_fiyat)

def babil_kitap():
    browser.get("https://www.google.com/")

    babilkitap_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    babilkitap_veri_girisi.send_keys(kitap_adi+ " "+ yayin_evi+ " "+" site:babil.com")
    time.sleep(2)

    babilkitap_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    babilkitap_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div/div[1]/a/h3")
    babilkitap_tikla.click()

    babilkitap_sayfa = browser.page_source

    babilkitap_soup = BeautifulSoup(babilkitap_sayfa, "lxml")
    
    babilkitap_yazar_adi=babilkitap_soup.find("h2",attrs={"class":"author"}).text
    babilkitap_yayin_evi=babilkitap_soup.find("h3",attrs={"class":"store"}).text
    babilkitap_kitap_adi=babilkitap_soup.find("h1",attrs={"itemprop":"name"}).text
    babilkitap_fiyat=babilkitap_soup.find("span",attrs={"class":"new-price mb10"}).text

    
    print("BABİL KİTAP = "+babilkitap_yazar_adi+","+babilkitap_yayin_evi+","+babilkitap_kitap_adi+","+babilkitap_fiyat)

def kitapsec():
    browser.get("https://www.google.com/")

    kitapsec_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    kitapsec_veri_girisi.send_keys(kitap_adi+ " "+ yayin_evi+ " "+" site:kitapsec.com")
    time.sleep(2)

    kitapsec_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    kitapsec_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div/div[1]/a/h3")
    kitapsec_tikla.click()

    kitapsec_sayfa = browser.page_source

    kitapsec_soup = BeautifulSoup(kitapsec_sayfa, "lxml")
    kitapsec_yazar_adi=kitapsec_soup.find("div",attrs={"itemprop":"author"}).text
    kitapsec_kitap_adi=kitapsec_soup.find("h1",attrs={"itemprop":"name"}).text
    kitapsec_fiyat=kitapsec_soup.find("span",attrs={"class":"fiyati"}).text
    print("KİTAPSEC = "+kitapsec_yazar_adi+","+kitapsec_kitap_adi+" ,"+kitapsec_fiyat)
    
    


babil_kitap()

bkm_kitap()  
kitapyurdu()
dr_kitap()
kitapsec()  