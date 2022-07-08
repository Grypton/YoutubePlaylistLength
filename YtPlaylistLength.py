'''
            
            
            This method doesn't use any api or anything. It is the most bruteForce method to find the same 
            
            
'''
import requests
from bs4 import BeautifulSoup as bs

# making a rewuest for playlist url and parsing its in the form of html
url = input("Enter the url of the Playlist : ")
r = requests.get(url)
soup = bs(r.content, 'html.parser')

#getting title of the playlist
title = soup.find("title").text
print()
print(title[:-10])

# finding the length of particular playlist by searching a particular text which contains time 
tags = soup.findAll("script")
tags = str(tags)
search = 'thumbnailOverlayTimeStatusRenderer":{"text":{"accessibility":{"accessibilityData":{"label":'
first = tags.find(search)
seconds = 0
count=0
dont_print =0
while first!= -1:
    tag1 = tags[first:first+150]  #approx length which contains time of particular videos 
    second = tag1.find("simpleText")
    tag1 = tag1[second+13:second+28] #since the time is contained in a quote (extracting it using find function)
    quote = tag1.find('"')
    time = tag1[:quote]
    time =list(time.split(":")) # list of time with seperated hours, minutes and seconds

    # converting whole time into second to finally sum it at the end  
    sum=0
    for i in range(1,len(time)+1):
        sum+= int(time[-i])*(60**(i-1))
    seconds +=sum
    count+=1 # count of no of videos in that playlist
    # doesn't print anything if count becomes greater than 100  
    if count==100:
        print()
        print("It contains more than 100 videos. Try it for playlist with less that 100 videos🙃")
        dont_print= 1
        break
    first = tags.find(search,first+100)

if dont_print==0:
    second_variation = [seconds,seconds//1.25,seconds//1.5,seconds//1.75,seconds//2]  #for different speeds

    print()
    print("No of Videos : ",count)

    print("Average per Video : ",end="")
 
    # time calculation for average per video
    seconds = seconds//count
    if (seconds<60):
        print(f"{int(seconds)} seconds")
    elif (seconds<3600):
        print(f"{round(seconds//60)} minutes, {int(seconds%60)} seconds")
    else :
        print(f"{round(seconds//(60*60))} Hours, {round((seconds%(60*60))//60)} minutes, {int((seconds%(60*60))%60)} seconds")


    # printing time for all different speeds 
    for i in range(len(second_variation)):
        if(i==0):
            print("Total length of Playlist : ",end="")
        if(i==1):
            print("At 1.25x : ",end="")
        if(i==2):
            print("At 1.50x : ",end="")
        if(i==3):
            print("At 1.75x : ",end="")
        if(i==4):
            print("At 2.00x : ",end="")
        if (second_variation[i]<60):
            print(f"{int(second_variation[i])} seconds")
        elif (second_variation[i]<3600):
            print(f"{round(second_variation[i]//60)} minutes, {int(second_variation[i]%60)} seconds")
        else :
            print(f"{round(second_variation[i]//(60*60))} Hours, {round((second_variation[i]%(60*60))//60)} minutes, {int((second_variation[i]%(60*60))%60)} seconds")


