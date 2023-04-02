from instagrapi import Client
from tiktok_uploader import uploadVideo
from youtube_upload.client import YoutubeUploader
import json

with open("config.json", "r") as file:
    config_data = json.load(file)

# Access data from the JSON object
title = config_data["title"]
description = config_data["description"]
tags = config_data["tags"]
video = config_data["video"]
instagram_credentials = config_data["instagram"]
tiktok_session_id = config_data["tiktok"]["sessionId"]

instagram = True
tiktok = True
youtube = False

# Upload video to youtube
if youtube:
  uploader = YoutubeUploader()
  uploader.authenticate()
  options = {
      "title" : title,
      "description" : description, 
      "privacyStatus" : "public", 
      "kids" : False, 
      "categoryId" : "24",
  }
  uploader.upload(video, options) 
  uploader.close()


if tiktok: 
  session_id = tiktok_session_id
  uploadVideo(session_id, video, title, tags)

if instagram:
  cl = Client()
  cl.login(instagram_credentials["username"], instagram_credentials["password"])
  cl.video_upload_to_story(video)
  cl.clip_upload(video, title)


