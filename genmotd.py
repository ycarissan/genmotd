#-*- coding: utf-8 -*-

#from https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

import xml.etree.ElementTree as ET
import argparse
import datetime

def setup_from_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("filename")
   parser.add_argument('--mode', type=int , help='mode 0:default')
   parser.set_defaults(mode=0)
   args = parser.parse_args()
#   print(args.filename)
   return args.filename, args.mode

def printNews(news):
   date_val=news.find('date').text.strip()
   txt_val=news.find('txt').text.strip()
   print("%s" % date_val)
   print("%s\n" % txt_val)

def main():
   filename, mode = setup_from_args()
   try:
      open(filename)
   except IOError:
      print("could not read", filename)
      exit()
   try:
      tree = ET.parse(filename)
   except:
      print("could not parse XML", filename)
      exit()
   root = tree.getroot()
   
   if (mode<=2):
      print("%s\n" % root.find('head').find('txt').text.strip())
   
   if (mode==0): #Default : ALL
      for news in root.findall('news'):
         printNews(news)
   elif (mode==1): #fresh news: earlier then 1 week
      for news in root.findall('news'):
         date_val=news.find('date').text.strip()
         datetime_object = datetime.datetime.strptime(date_val, '%Y-%m-%d %H:%M')
         if (datetime.datetime.today() - datetime_object < datetime.timedelta(days=7)):
            printNews(news)

   else:
      print("Mode unknown: %i\n",mode)

if __name__ == "__main__":
   main()
