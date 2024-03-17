import music21

f = music21.note.Note("F5")

print(f)
print(f.transpose("m3"))

music21.note.Note("C4").show("midi")
