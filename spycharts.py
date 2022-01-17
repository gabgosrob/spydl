from user import User

def main() -> None:
	username = input("username: ")
	password = input("password: ")
	user = User(username, password)

	photos = user.get_all_photos()
	for photo in photos:
		user.download_photo(photo)

if __name__ == "__main__":
	main()
