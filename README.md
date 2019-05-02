# 3cx-selfidprompt-gen
A self_prompt_id.wav generator for 3CX

This script will find extension folders without a `self_id_prompt.wav` and generate one based on the name in the `users.json` file for each extension.

This should work on Linix, macOS and probably even Windows.

#) Grab all the extension folders from your 3CX server at `/var/lib/3cxpbx/Instance1/Data/Ivr/Voicemail/Data`
$) **Make a backup of these folders**
#) Make a new directory for the project, create a `data` folder inside of it.
#) Install `ffmpeg` for your OS i.e. `brew install ffmpeg`
#) Install the required Python libs: i.e. `sudo pip install gTTS pydub`
#) Place all your extension folders into the `data` folder.
#) Create a `users.json` folder in the project folder with the same format as `users.json.example`
#) Run `python self_id.py`
#) SFTP the folders back into the source folder
#) On the 3CX server, make sure to `chown phonesystem:phonesystem * -R` to repair permissions.
#) Test!

Everything worked perfect for me after I fixed the sample rate, your mileage may vary.


Remember to  the uploaded files in the source directory if you're using SFTP, otherwise they'll probably give you permissions problems in the future.

Enjoy :)

***Disclaimer: I offer no warranty for the provided code, run at your own risk. Really thought it's fine, but... if you screw it up, it ain't on me!! :)***
