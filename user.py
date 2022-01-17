import requests
from typing import List
from spypoint import Client, Photo

class User:
	def __init__(self, username: str, password: str) -> None:
		self.client = self.login(username, password)

	def login(self, username: str, password: str) -> Client:
		return Client(username, password)

	def get_all_photos(self) -> List[Photo]:
		return [p for p in self.client.photos(self.client.cameras())]
