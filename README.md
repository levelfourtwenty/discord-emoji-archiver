# discord-emoji-archiver
A simple python script which can be used to archive all of the emojis within a server. 

The script is intentionally simple as I wrote it for a one time use. I am not planning on changing it further. 


### Usage

1. Install the required python modules using `$ pip install -r requirements.txt`.
2. Edit `bot.py` to include your token and secret string. If you do not change the secret string you can risk someone accidentally triggering your bot.
3. Run the bot with `$ python bot.py`. Be aware that the script requires a minimum python version of 3.10.
4. Send a message containing your secret string and only your secret string in the server of which you intend to archive it's emotes.

The bot will create a subdirectory within the directory where `bot.py` is situated in which the emojis will be saved to. 
