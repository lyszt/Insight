import sys
import pickle
from _ast import Lambda

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

edge_options = EdgeOptions()
edge_options.use_chromium = True

edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
app = tk.Tk()
app.title('Ferramenta de Busca - β1')
app.geometry("800x500")
app.iconbitmap("FaviconAlt3.ico")
Googling = False
IQ = tk.Entry(app, width=100, borderwidth=15 , relief=tk.FLAT, bg="lightgrey")
IQ.pack()
IQ.insert(0, "O que você está procurando?")

AuthorCopy = Label(app, text="Mactab 2021 © Todos os direitos reservados.")
AuthorCopy.pack()
L1 = Listbox(app)

def InitialQuestion():

    L1.delete(0, tk.END)



    browser = Edge(executable_path=r"C:\Users\ADM\MSEDGEWEBDRIVER\MicrosoftWebDriver.exe", options=edge_options)



    browser.get("https://www.google.com")
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)

    time.sleep(5)

    browser.find_element_by_name("q").send_keys(IQ.get())
    time.sleep(5)
    browser.find_element_by_name("q").send_keys(Keys.ENTER)
    results_list = browser.find_elements_by_xpath('//div[@class="g"]//a')
    i = 0





    def OpenURL(event):
        weblink = L1.get(ACTIVE)
        webbrowser.open(weblink)

    for item in results_list:

        Attribute = [item.get_attribute('href') for results_list in browser.find_elements_by_xpath('//div[@class="yuRUbf"]/a')]

        for items in Attribute:
            L1.insert(i, items)
            i += 1




        if i == 100:
            browser.find_element_by_id("pnnext").click()

            for item in results_list:

                Attribute = [item.get_attribute('href') for results_list in
                             browser.find_elements_by_xpath('//div[@class="yuRUbf"]/a')]

                for items in Attribute:


                    L1.insert(i, items)


                    i += 1

                if i == 100:
                    for item in results_list:

                        Attribute = [item.get_attribute('href') for results_list in
                                 browser.find_elements_by_xpath('//div[@class="yuRUbf"]/a')]

                    for items in Attribute:
                        L1.insert(i, items)

                        i += 1

                    if i == 100:
                        break
                    break
            break


    browser.quit()



    L1.bind("<Double-Button-1>", OpenURL)
    L1.pack(expand=True, fill=BOTH)


Button = tk.Button(app, text="Enviar", padx = 40, pady = 2, command=InitialQuestion, bg='lightgreen')
Button.pack()



app.mainloop()











