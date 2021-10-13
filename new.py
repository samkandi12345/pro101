import dropbox
class DataMove:
    def __int__(self,access_token):
        self.access_token = access_token

    def UploadFiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        file = open(file_from,"rb")
        dbx.files_upload(file.read(),file_to)

def main():
    access_token = "sl.A6RXZI4cvBAtAUi4KfTttPGB254P6VEvZYlfgSBug-CbAad20vVTiPSZ1Z-C4Uc42IufHb6SA5DLOPcT8bnxnGXNSzYukpqBpDWSjdT_iQ84upowRFOIS5jD5JHISsgdvxqCFMA"
    createtransferdata = DataMove(access_token)
    file_from = input("enter the file: ")
    file_to = input("enter the path to transfer the file")
    createtransferdata.UploadFiles(file_from,file_to)
    print("The file has been moved ")

main()


