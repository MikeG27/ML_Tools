from google_drive_downloader import GoogleDriveDownloader as gdd


def download_file(file_id,dest_path,unzip=True):
    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=dest_path,
                                        unzip=unzip)
    print("/ Data was downloaded ")




if __name__ == "__main__":
    file_id = '1E6YhO0sCFUbNOs_4IpgS4uq_ZcuYb_e1'
    dest_path = 'data/Panel ChallengING.zip'
    download_file(file_id,dest_path)