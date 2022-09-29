# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:31:59 2022

@author: mikol
"""
import io

def clearACReview(nameOfOrigFile,nameOfDestFile):
# This function converts raw scan from website into clear reviews of Assasin's Creed games
    
    nameOfOrigFile = io.open(nameOfOrigFile+".txt", mode="r", encoding="UTF-8")

    nameOfDestFile = io.open(nameOfDestFile+".txt", mode="w+", encoding="UTF-8")

    for x in nameOfOrigFile:
        if "ass" and "Ass" and "ac" and "AC" in x:
            nameOfDestFile.write(x+"\n") 

    nameOfDestFile.close()
    nameOfOrigFile.close()
    return print("Operation done. Check TXT files.")

def clearHOMMReview(nameOfOrigFile,nameOfDestFile):
# This function converts raw scan from website into clear reviews of HoMM games

    nameOfOrigFile = io.open(nameOfOrigFile+".txt", mode="r", encoding="UTF-8") 
    nameOfDestFile = io.open(nameOfDestFile+".txt", mode="w+", encoding="UTF-8")
    
    for x in nameOfOrigFile:
        if "heroes" and "Heroes" and "HOMM" and "homm" in x:
            nameOfDestFile.write(x+"\n")
    
    nameOfDestFile.close()
    nameOfOrigFile.close()
    return print("Operation done. Check TXT files.")

def UniqueFeature(nameOfReviewFile,nameOfDestFile):
#This function shows the unique features o games   
    
    nameOfReviewFile = io.open(nameOfReviewFile+".txt", mode="r", encoding="UTF-8")
    nameOfDestFile = io.open(nameOfDestFile+".txt", mode="w+", encoding="UTF-8")
    
    features = ["good","bad","pros","con","flaw","uniqe","mechan","graph","sound","music","feature","character","special","main","advantage","love","enjoy","hate","favour","great","disaster","move","espec","appro","best","worst"]
    
    for unique in nameOfReviewFile:
        if "{}".format(x for x in features) in unique:
            nameOfDestFile.write(unique+"\n")
    
    nameOfDestFile.close()
    nameOfReviewFile.close()
    return print("Operation done. Check TXT files.")
                