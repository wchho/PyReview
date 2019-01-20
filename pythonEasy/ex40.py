class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics: # lyrics lists organized so there's a line per item
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
print(happy_bday.lyrics) # prints the lyric list

bulls_on_parade.sing_me_a_song()
print(bulls_on_parade.lyrics)
