import os
import mimetypes

def validateImage(file):
    extension = os.path.splitext(file)[1]
    validExtensions = ['.jpg', '.gif', '.png', '.jpeg']
    if not extension in validExtensions:
        print('not allowed')

def validateAudio(file):
    extension = os.path.splitext(file)[1]
    extension = extension.lower()
    validExtensions = ['.mp4', '.mp3', '.wav', '.flac', '.m4a']
    if not extension in validExtensions:
        print('not allowed')
