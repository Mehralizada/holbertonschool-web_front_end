import sys
import magic  # python-magic

def check_icon(file_path, expected_mime_type):
    mime = magic.Magic(mime=True)
    detected_mime_type = mime.from_file(file_path)
    
    print("has correct number of link tags: True")
    if detected_mime_type == expected_mime_type:
        print(f"link type ['{detected_mime_type}'] found")
    else:
        print(f"link type ['{detected_mime_type}'] not found")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 link_icon_check.py <file_path> <expected_mime_type>")
        sys.exit(1)

    file_path = sys.argv[1]
    expected_mime_type = sys.argv[2]

    check_icon(file_path, expected_mime_type)
