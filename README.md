
# Instagram Photo Downloader

This project allows you to download all photos from an Instagram profile and save them in a single ZIP file. This script uses the `instaloader` library to fetch the images without creating any metadata files or directories.

## Features

- Downloads all photos from a given Instagram profile.
- Saves the photos in a ZIP file.
- Does not create any metadata files or directories.

## Requirements

- Python 3.x
- `instaloader` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/instagram-photo-downloader.git
    cd instagram-photo-downloader
    ```

2. Install the required library:
    ```bash
    pip install instaloader
    ```

## Usage

Run the script and provide the Instagram username when prompted:

```bash
python main.py
```

You will be asked to enter the Instagram username. The script will download all photos from the profile and save them in a ZIP file named after the username.

## Example

```bash
$ python main.py
Enter the Instagram username: exampleusername
Downloading photos from Instagram profile: exampleusername
All photos downloaded and saved to exampleusername.zip
```

## Note

- Ensure you have the necessary permissions to download photos from the Instagram profile you specify.
- This script does not support downloading photos from private profiles.
