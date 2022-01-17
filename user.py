import requests
from typing import List
from spypoint import Client, Photo
from utils import save_image_from_data

class User:
	def __init__(self, username: str, password: str):
		self.client = self.login(username, password)

	def login(self, username: str, password: str) -> Client:
		return Client(username, password)

	def get_all_photos(self) -> List[Photo]:
		return [p for p in self.client.photos(self.client.cameras())]

	def download_photo(self, photo: Photo) -> None:
		data = self.get_photo_data(photo)
		save_image_from_data(data, photo.originName)

	def get_photo_data(self, photo: Photo) -> bytes:
		return requests.get(photo.url()).content
