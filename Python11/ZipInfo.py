import sys
import io 
import zipfile

data = bytes.fromhex(sys.stdin.read().replace(' ', '').replace('\n', ''))
files = [file for file in zipfile.ZipFile(io.BytesIO(data)).infolist() if not file.is_dir()]
print(len(files), sum(file.file_size for file in files), end='')
