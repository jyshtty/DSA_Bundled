import os
import shutil

def count_files_in_directory(directory):
    file_count = 0

    for _, _, files in os.walk(directory):
        file_count += len(files)
        for i in files:
            if "py" in i:
                dir_name = i.split(".")[0]
                with open("README.md", 'w') as file:
                    file.write("# " + dir_name[3:])
                os.mkdir(dir_name )
                shutil.move(i, dir_name)
                shutil.move("README.md", dir_name)
        print(files)

    return file_count

# Example usage
directory_path = "/Users/apple/Documents/DSA_Bundled/Searching_Sorting/Binary_Search"
file_count = count_files_in_directory(directory_path)
print(f"Number of files in directory: {file_count}")
#
#
#
#
# import os
# def check_filesystem_permissions(path):
#     try:
#         stat_info = os.statvfs(path)git
#         permissions = stat_info.f_flag
#         is_read_only = permissions & (os.ST_RDONLY | os.ST_NOSUID)
#
#         if is_read_only:
#             print("File system is read-only.")
#         else:
#             print("File system is writable.")
#
#     except Exception as e:
#         print(f"Error occurred while checking file system permissions: {str(e)}")

# check_filesystem_permissions("/Users/apple/Documents/DSA_Bundled/Searching_Sorting/Binary_Search/")







