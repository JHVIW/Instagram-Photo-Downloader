import instaloader
import os
import zipfile

def download_instagram_photos(username):
    # Initialize Instaloader
    L = instaloader.Instaloader(download_videos=False, download_comments=False, save_metadata=False, download_geotags=False, compress_json=False)

    # Create a temporary directory
    temp_dir = f"{username}_temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Download profile
    try:
        print(f"Downloading photos from Instagram profile: {username}")
        profile = instaloader.Profile.from_username(L.context, username)
        for post in profile.get_posts():
            L.download_post(post, target=temp_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Create a zip file
    zip_filename = f"{username}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    zipf.write(os.path.join(root, file), file)

    # Remove the temporary directory
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            os.remove(os.path.join(root, file))
    os.rmdir(temp_dir)

    print(f"All photos downloaded and saved to {zip_filename}")

if __name__ == "__main__":
    user = input("Enter the Instagram username: ")
    download_instagram_photos(user)
