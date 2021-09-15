from pytube import YouTube
import os
from pathlib import Path
import time
while True:

   answer = input("What would you like to do?\nType '1' for downloading a video in MP4 format.\nType 'q' to exit the program.\n")
   if answer == str("1"):
      link = input("Please enter the Youtube-Video link. Make sure to type in the whole link, including 'https'.\n")
      try:
         url = YouTube(link)
      except:
         print("\nThat is not a valid link, restarting process.\n")
         continue
      print(f"Downloading '{url.title}'...")
      video = url.streams.get_highest_resolution()
      path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
      video.download(path_to_download_folder)
      print("\nSuccessfuly downloaded the video into the downloads folder.\n")
      continue
   
   if answer == str("q"):
      print("Closing program, thanks for using!")
      time.sleep(1.5)
      break
   
   else:
      print("That is an invalid answer, restarting program:\n")