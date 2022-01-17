import requests
from typing import List
from getpass import getpass
from user import User
from spypoint import Photo
from utils import save_image_from_data

def main() -> None:
	username = input("username: ")
	password = getpass("password: ")
	
	try:
		user = User(username, password)
		photos = user.get_all_photos()
		print("Downloading...")
		download_all_photos(photos)
		print("Done!")
	except Exception as e:
		print("Something went wrong. Check your login info or try again later.")

def download_all_photos(photos: List[Photo]) -> None:
	for photo in photos:
		download_photo(photo)

def download_photo(photo: Photo) -> None:
	data = get_photo_data(photo)
	save_image_from_data(data, photo.originName)

def get_photo_data(photo: Photo) -> bytes:
	return requests.get(photo.url()).content

if __name__ == "__main__":
	main()
