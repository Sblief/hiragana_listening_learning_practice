import os, random, pygame 




def sound_play(path):
	# play an alarm sound
	pygame.mixer.init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.play()


directory = os.path.dirname(os.path.abspath(__file__))+"\sounds\\"
# print(directory)

hiragana_dict = {}

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filename_without_ext = os.path.splitext(filename)[0]
    if filename.endswith(".mp3"): 
        hiragana_dict[filename_without_ext] = directory+filename
    else:
        continue


hiragana_dict_copy = hiragana_dict
while True:
    random_hiragana = random.choice(list(hiragana_dict_copy.items()))
    sound_play(random_hiragana[1])
    break




