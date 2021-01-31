import os

import pyfiglet
from pytube import YouTube, Playlist

file_size = 0
folder_name = ""


# Progress Bar
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if iteration == total:
        print()


# Show Progress Bar
def show_progress_bar(chunk, file_handle, bytes_remaining):
    print_progress_bar(file_size - bytes_remaining, file_size, prefix='Progress:', suffix='Complete', length=50)
    return


# Get Download Location
def get_download_location():
    if os.name == 'nt':
        download_location = os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        download_location = os.path.join(
            os.path.expanduser('~'), 'Downloads')
    return download_location


# Get Desired Resolution
def get_resolution(video_url):
    yt_obj = YouTube(video_url, on_progress_callback=show_progress_bar)
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    print("\nAvailable Resolutions -")
    for num, res in enumerate(filters, start=1):
        print("\t{}. {}".format(num, str(res.resolution)))
    selected_res = int(input('Please enter desired resolution : '))
    filters = filters[selected_res - 1]
    return filters


# Single Video Download
def download_video():
    global file_size
    try:
        video_url = input('Provide Video Download Link : ')
        filters = get_resolution(video_url)
        file_size = int(filters.filesize)
        download_location = get_download_location()
        print("\nDownloading {}".format(str(filters.title)))
        filters.download(output_path=download_location)
        print("Video Downloaded. Thanks for using!!\nYou can find the video here - {}".format(download_location))
    except Exception as e:
        print("Some Error occured. Exception message is : ", e)


# Playlist Single Video Download
def download_playlist_video(video_url, res):
    global file_size
    yt_obj = YouTube(video_url, on_progress_callback=show_progress_bar)
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4', resolution=res).first()
    file_size = int(filters.filesize)
    if not filters:
        filters = yt_obj.streams.filter(
            progressive=True, file_extension='mp4').first()
    print("\nDownloading {}".format(str(filters.title)))
    download_location = get_download_location()
    filters.download(output_path="{}/{}".format(download_location, folder_name))
    print("Download Complete")


# Playlist Download
def download_playlist():
    global folder_name
    try:
        playlist_url = input('Provide Playlist Link : ')
        videos_list = Playlist(playlist_url)
        folder_name = videos_list.title
        resolution = get_resolution(videos_list[0]).resolution
        for video in videos_list:
            download_playlist_video(video, resolution)
        print("All Videos Downloaded. Thanks for Using!!")
    except Exception as e:
        print("Some Error occurred. Exception message is : ", e)


# Main Function
def main():
    ascii_banner = pyfiglet.figlet_format("YT Downloader")
    print(ascii_banner)
    print("\t By Pratik Panda\n\n")
    choice = int(input(
        """MENU
1.Download Single Video
2.Download Playlist\n
Enter Your Choice : """))
    if choice == 1:
        download_video()
    elif choice == 2:
        download_playlist()
    else:
        print("Wrong Option")


# Start of Program
if __name__ == '__main__':
    main()
