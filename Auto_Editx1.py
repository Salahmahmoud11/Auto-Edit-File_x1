#Code By Zoro_RCE [20/6/2025]

import os
import shutil

target_path = input("Enter Path ")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}

if not os.path.isdir(target_path):
    print("Error Path")
else:
    for category in categories:
        folder_path = os.path.join(target_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for item in os.listdir(target_path):
        item_path = os.path.join(target_path, item)

        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()

            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(target_path, category)
                    shutil.move(item_path, destination_folder)
                    print(f" Move: {item} -> {category}")
                    break 

    print("Done\n")