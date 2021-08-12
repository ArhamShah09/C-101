import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'ScCnNIeInuUAAAAAAAAAAShZGoNpDyRkSfkOGJx7UaG_SeLI4Uq4KmPoVCqoRrJQ'
    transferData = TransferData(access_token)

    file_from = input("Enter your source file : ")
    file_to = input("Enter your file destination : ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been uploaded.")

main()