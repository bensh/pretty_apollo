# pretty_apollo
Prettification of Apollo tool (https://github.com/mac4n6/APOLLO) allowing for the easier interpretation of associated output. 
This is in the form of a .txt file, but the standard output of SQL and CSV are still available for forensics verification of evidence.

# Usage
Can be used in interactive mode for all options, or headless mode (--head) which uses yolo mode for platform and version.
	
  - Interactive: python pretty_apollo.py
  - Headless: python pretty_apollo.py --head -o {sql|csv} -mod_dir PATH_TO_MODULES PATH_TO_DATA

# Output
  - csv - CSV
  - sql - SQLite Database
  - txt - txt file of the data in a more readable format
  
# Platform Options (-p)
  - iOS
  - Mac
  - Yolo - Parse everything

# Version Options (-v)
  - iOS 8, 9, 10, 11, 12
  - Yolo - Parse everything
  
# Credits
Apollo Author: Sarah Edwards | @iamevltwin | mac4n6.com
