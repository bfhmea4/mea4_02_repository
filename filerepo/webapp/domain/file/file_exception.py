class FileNotFoundError(Exception):
    message = "The file you specified does not exist."

    def __str__(self):
        return FileNotFoundError.message


class FilesNotFoundError(Exception):
    message = "No files were found."

    def __str__(self):
        return FilesNotFoundError.message