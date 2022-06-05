import requests
import json
import time
import calendar
import pyperclip
import locale
locale.setlocale(locale.LC_TIME,'fr_FR')


def Logger(level,message):
    print("["+str(level)+" - "+ str(time.strftime('%d/%m/%Y %H:%M:%S'))+"] : "+str(message))


def BibTexGenerator(json):
    ## URL
    URL ="howpublished={\\url{"+ JSON_LOAD['URL']+ "} },"
    
    ### Author  
    AUTHORS = " and ".join([f"{author['family']}{','} {author['given']}" for author in JSON_LOAD["author"]])
    AUTHORS = "author={"+AUTHORS+"},"

    
    ### Title
    TITLE = "title={"+JSON_LOAD['title']+"},"

    ### Year/Month
    temp_date=JSON_LOAD['created']
    temp_date=temp_date['date-parts'][0]
    DATE="month={"+str(calendar.month_name[int(temp_date[1])])+"},\n"+"year={"+str(temp_date[0])+"},"


    ## ID
    KEY = "article:"+str(JSON_LOAD["prefix"])+"_"+str(temp_date[1])+"_"+str(temp_date[0])

    ## Note
    NOTE ="note={ [En Ligne] - consulté le "+ time.strftime('%d') +" "+ calendar.month_name[int(time.strftime("%m"))] + " "+ time.strftime("%Y")+" }"

    ## Final display
    FINAL="\n@misc{"+KEY+",\n"+AUTHORS+"\n"+TITLE+"\n"+URL+"\n"+DATE+"\n"+NOTE+"}\n"

    pyperclip.copy(FINAL)
    Logger("INFO","BibTex copy to your clipboard")
    print("\n\n\n Result \n\n\n")
    print(FINAL)



print("Enter DOI Number Only URL")
DOI_URL = input()
Logger("INFO", "Wait for DOI Lookup")


## GET JSON file
PARAMETER={'Accept': 'application/vnd.citationstyles.csl+json'}

DOI_REQUEST = requests.get(DOI_URL,headers=PARAMETER)
JSON_DOI=DOI_REQUEST.text

if(DOI_REQUEST.status_code==200):
    Logger("INFO", "HTTP Status Code :"+str(DOI_REQUEST.status_code))
    JSON_LOAD = json.loads(JSON_DOI)
    BibTexGenerator(JSON_LOAD)

else:
    Logger("ERROR","Something Wrong - HTTP Status Code :"+str(DOI_REQUEST.status_code))


