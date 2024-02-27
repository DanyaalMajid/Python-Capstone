import requests
from tqdm import tqdm

def download_file(url, filename):
    response = requests.get(url, stream=True)

    total_size_in_bytes= int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    with open(filename, 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

# Use the function
download_file('https://ash-speed.hetzner.com/100MB.bin', '100MB.bin')