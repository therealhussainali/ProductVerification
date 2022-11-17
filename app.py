import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tkinter import *
import validators


def Main():
    import tkinter as tk

    root= tk.Tk()

    root.attributes('-fullscreen', True)
    canvas1 = tk.Canvas(root, width=1920, height=1080, relief='raised', bg='white')
    canvas1.pack()

    label1 = tk.Label(root, text='PRODUCT VERIFICATION')
    label1.config(font=('lucida', 50, 'bold'))
    canvas1.create_window(960, 50, window=label1)

    label2 = tk.Label(root, text='Type your Web link:')
    label2.config(font=('lucida', 17 , 'bold'))
    canvas1.create_window(960, 160, window=label2)

    entry1 = tk.Entry(root) 
    canvas1.create_window(960, 230, window=entry1)

    def Verification():
        supported_sites = 'daraz.pk'
        web_link = entry1.get()

        label3 = tk.Label(root, text=f'Your Product is', font=('helvetica', 15))
        label4 = tk.Label(root, text=f'Your Product Price is and the ratings are ', font=('helvetica', 25))
        label5 = tk.Label(root, text=(f''), font=('helvetica', 30))
        label_warning = tk.Label(root, text='ERROR: Invalid Link, Please only use daraz.pk links', font=('helvetica', 25))

        if (web_link != None and validators.url(web_link) and supported_sites in web_link):
            product_details = getElements(web_link)

            if (label_warning.winfo_exists()):
                label_warning.destroy()

            label3 = tk.Label(root, text=f'Your Product is {product_details[0].text}', font=('helvetica', 15))
            label4 = tk.Label(root, text=f'Your Product Price is {product_details[1].text} and the ratings are {product_details[2].text}', font=('helvetica', 25))
            label5 = tk.Label(root, text=(f'{result}'), font=('helvetica', 30))

            canvas1.create_window(960, 300, window=label3)
            canvas1.create_window(960, 350, window=label4)

            ratings = product_details[2].text
            ratings = ratings.replace('Ratings', '')
            ratings = ratings.strip()
            print(ratings)
            result = Product_Validation(int(ratings))

            
            canvas1.create_window(960, 400, window=label5)

        else:
            if (label3.winfo_exists() and label4.winfo_exists() and label5.winfo_exists()):
                label3.destroy()
                label4.destroy()
                label5.destroy()

            
            canvas1.create_window(960, 300, window=label_warning)
        
    button1 = tk.Button(text='Verify Product', command=Verification, bg='green', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(960, 260, window=button1)

    root.mainloop()

def getElements(weblink):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(weblink)

        product_name = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[3]/div/div/span')
        product_price = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[7]/div/div/span')
        product_rating = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[4]/div[1]/div/div/a[1]')
        print(f'Product Name: {product_name.text}\nProduct Price: {product_price.text}\nProduct Rating: {product_rating.text}')
        return product_name, product_price, product_rating
    except:
        return "ERROR"

def Product_Validation(ratings : int):
    if (ratings < 10 ):
        result = "0/10 Score - This product is likely to be broken or malfunctioning"
        return result
    elif (ratings < 50 and ratings > 10):
        result = "2/10 Score - The Product is Scam Likely [DO NOT BUY]"
        return result
    elif (ratings < 150 and ratings > 50):
        result = "5/10 Score - The Product is slightly trustable [BUY AT YOUR OWN RISK]"
        return result 
    elif (ratings < 300 and ratings > 150):
        result = "8/10 Score - This product is trust-worthy and you can buy it safely"
        return result
    else:
        result_final = "10/10 Score - This product is definitely trustable"
        return result_final


if __name__ == '__main__':
    Main()