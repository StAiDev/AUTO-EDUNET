pyinstaller --onefile -n autoE --noconsole --icon icon/ico.ico --add-data "modules/*;./modules" --add-data "resources/*;./resources" --add-data "downloads/*;./downloads" main.py