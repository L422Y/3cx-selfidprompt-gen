from pydub import AudioSegment
from gtts import gTTS
import os, json

datadir = 'data'

# load users
with open('users.json', 'r') as f:
	users = json.load(f)

# find missing self id prompts
for subdir, dirs, files in os.walk(datadir):
	if subdir != datadir:
		# determine name
		ext = subdir.replace("data/", "")
		if ext in users:
			name_text = users[ext]
			# if this extension folder has no prompt
			if "self_id_prompt.wav" not in files:
				print "Creating self_id_prompt for '%s' (ext. %s)" % (name_text, ext)
				# generate self_id_prompt for extension
				tts = gTTS(text=name_text, lang='en')
				tts.save("temp.mp3")
				sound = AudioSegment.from_mp3("temp.mp3")
				sound = sound.set_frame_rate(8000)
				sound.export("%s/self_id_prompt.wav" % subdir, format="wav")
			else:
				print "Skipping existing prompt for '%s' (ext. %s)" % (name_text, ext)
		else:
			print "Skipping extension with missing name (ext. %s)" % (ext)

