import os

def rename_files(folder_path, filename_to_remove):
  """Renames all files in the given folder path, removing the given string.

  Args:
    folder_path: The path to the folder containing the files to rename.
  """

  for filename in os.listdir(folder_path):
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = old_file_path.replace(filename_to_remove, '')

    os.rename(old_file_path, new_file_path)

if __name__ == '__main__':
  folder_path = ''
  filename_to_remove = ''

  rename_files(folder_path, filename_to_remove)
