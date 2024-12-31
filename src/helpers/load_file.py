def load_file(file_path: str) -> bytes:
    with open(file_path, "rb") as file:
        return file.read()
