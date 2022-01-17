import os

def save_image_from_data(data: bytes, name: str) -> None:
	file_path = f"photos/{name}"
	ensure_dir(file_path)
	with open(file_path, "wb") as handler:
		handler.write(data)

def ensure_dir(file_path: str) -> None:
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
