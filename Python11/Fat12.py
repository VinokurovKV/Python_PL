import sys
import struct

disk_image = sys.stdin.buffer.read()

if len(disk_image) != 1474560:
    exit()

BYTES_PER_SECTOR = 512
ROOT_ENTRIES_COUNT = 224
DIR_ENTRY_SIZE = 32

fat_area_size = 2 * 9 * BYTES_PER_SECTOR
root_directory_offset = 1 * BYTES_PER_SECTOR + fat_area_size
root_directory_size = ROOT_ENTRIES_COUNT * DIR_ENTRY_SIZE

directory_entries = []

current_pos = root_directory_offset
end_pos = root_directory_offset + root_directory_size

while current_pos < end_pos:
    entry_data = disk_image[current_pos:current_pos + DIR_ENTRY_SIZE]
    
    if entry_data[0] == 0:
        break
        
    if entry_data[0] != 0xE5 and not (entry_data[11] & 0x08):
        filename_part = entry_data[0:8].decode('cp866').rstrip()
        extension_part = entry_data[8:11].decode('cp866').rstrip()
        
        if extension_part:
            complete_filename = filename_part + '.' + extension_part
        else:
            complete_filename = filename_part
            
        complete_filename = complete_filename.rstrip()
        file_size_value = struct.unpack('<I', entry_data[28:32])[0]
        
        if entry_data[11] & 0x10:
            directory_entries.append((complete_filename, 'dir'))
        else:
            directory_entries.append((complete_filename, file_size_value))
    
    current_pos += DIR_ENTRY_SIZE

for i in range(len(directory_entries)):
    for j in range(i + 1, len(directory_entries)):
        if directory_entries[i][0] > directory_entries[j][0]:
            directory_entries[i], directory_entries[j] = directory_entries[j], directory_entries[i]

for entry in directory_entries:
    filename, size_info = entry
    if size_info == 'dir':
        print(f"{filename:12} dir")
    else:
        print(f"{filename:12} {size_info}")