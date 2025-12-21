import os
import shutil
import logging

# -------------------- LOGGING CONFIGURATION --------------------

log_file = os.path.join(os.getcwd(), "automation.log")

logger = logging.getLogger("FileAutomationLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("Logger initialized successfully")

# -------------------- FILE EXTENSION MAPPING --------------------
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

# -------------------- MAIN FUNCTION --------------------
def organize_files(folder_path):
    try:
        # Check if path exists
        if not os.path.exists(folder_path):
            print("Invalid path entered.")
            logging.error("Invalid directory path.")
            return

        # List all files in directory
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            moved = False
            file_extension = os.path.splitext(file)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(folder_path, folder)

                    # Create folder if not exists
                    if not os.path.exists(destination_folder):
                        os.mkdir(destination_folder)
                        logging.info(f"Created folder: {folder}")

                    shutil.move(file_path, destination_folder)
                    logging.info(f"Moved {file} to {folder}")
                    print(f"{file} moved to {folder}")
                    moved = True
                    break

            # If file type not matched
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(other_folder):
                    os.mkdir(other_folder)
                    logging.info("Created folder: Others")

                shutil.move(file_path, other_folder)
                logging.info(f"Moved {file} to Others")
                print(f"{file} moved to Others")

        print("File organization completed successfully.")
        logging.info("File organization completed.")

    except Exception as e:
        print("An error occurred. Check the log file.")
        logging.error(f"Error: {e}")

# -------------------- USER INPUT --------------------
if __name__ == "__main__":
    print("---- File Automation Script ----")
    path = input("Enter the directory path to organize: ")
    organize_files(path)
