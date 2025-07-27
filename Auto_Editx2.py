#Code By Zoro_RCE & Ai [21/6/2025]


import os
import shutil

target_path = input("Enter your Path: ").strip()

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    #"ADD_More_Categories": [],
    "Other": []  # Add list for Other file types or If you don't modify it, all remaining files not added to any categories will be automatically moved to the "Other" folder. 
                # You can add other categories to the code, such as "categorie for videos."
}

if not os.path.isdir(target_path):
    print(f"Error: '{target_path}' is not a valid directory.")
else:
    for category in categories:
        folder_path = os.path.join(target_path, category)
        os.makedirs(folder_path, exist_ok=True)  # exist_ok prevents errors if folder exists

    moved_files = 0
    for item in os.listdir(target_path):
        item_path = os.path.join(target_path, item)

        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()

            destination_category = "Other"  # Default For Other
            for category, extensions in categories.items():
                if category != "Other" and file_extension in extensions:
                    destination_category = category
                    break

            destination_path = os.path.join(target_path, destination_category, item)
            
            # Handle file name conflicts
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(item)
                counter = 1
                new_filename = f"{base}_{counter}{ext}"
                destination_path = os.path.join(target_path, destination_category, new_filename)
                
                # Keep incrementing until a unique name is found
                while os.path.exists(destination_path):
                    counter += 1
                    new_filename = f"{base}_{counter}{ext}"
                    destination_path = os.path.join(target_path, destination_category, new_filename)
            
            try:
                shutil.move(item_path, destination_path)
                print(f"Moved: {item} -> {destination_category}")
                moved_files += 1
            except (shutil.Error, OSError) as e:
                print(f"Error moving {item}: {e}")
        else:
            print(f"Skipped: {item} (Not a file)")

    # Summary of operation
    if moved_files == 0:
        print("No files were moved.")
    else:
        print(f"\nCompleted: {moved_files} file(s) moved successfully.")