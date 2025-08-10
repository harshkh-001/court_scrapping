from django.shortcuts import render,HttpResponse,redirect
from django.http import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from .models import CaseData


url = "https://delhihighcourt.nic.in/app/get-case-type-status"


def redirects(request):
    return redirect(home)

def home(request):
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.content , 'html.parser')
        
        options = soup.find(id="case_type")
        years = soup.find(id="case_year")
        values = [option.get("value") if(option.get("value")) else "select" for option in options.find_all("option")]
        years = [year.get("value") if(year.get("value")) else "select" for year in years.find_all("option")]
        return render(request, "info/base.html", {"values":values , "years" : years})
    return HttpResponse("site not accessable try later ( site down )")



def form_handle(request):
    if(request.method == "POST"):
        # print(request.POST)
        case_type = {request.POST.get("case_type")}
        case_number = {request.POST.get("case_number")}
        case_year = {request.POST.get("years")}
        
        options = Options()
        options.add_argument("--headless")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(url)
        
        driver.find_element(By.ID, "case_type").send_keys(case_type)
        driver.find_element(By.ID,"case_number").send_keys(case_number)
        driver.find_element(By.ID, "case_year").send_keys(case_year)
        capcha = driver.find_element(By.CLASS_NAME, "captcha-code").text
        driver.find_element(By.ID, "captchaInput").send_keys(capcha)
        # time.sleep(2)
        button = driver.find_element(By.ID, "search")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        # time.sleep(1)
        driver.execute_script("arguments[0].click();", button)
        
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "caseTable"))
        )
        
        headings = table.find_elements(By.CLASS_NAME, "dt-column-title")
        head = [heading.text.strip() for heading in headings]
        # print("heading : ")
        # print(head)
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        all_data = [] 
        raw_data_lines = [] 
        # return HttpResponse(rows)
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            data = [cell.text.strip() for cell in cells]
            if data:
                all_data.append(data)
                raw_data_lines.append("|".join(data)) 
                # print(data)
        
        raw_data = "\n".join(raw_data_lines)
        # print(raw_data)
        driver.quit()
        CaseData.objects.create(case_type=case_type , case_number=case_number , year=case_year, result=raw_data)
        return render(request, "info/showtable.html" , {"head":head , "data":all_data})
    return HttpResponse("unknown Error occur please try again later")