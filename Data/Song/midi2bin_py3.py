import sys
import mido

pattern = mido.MidiFile(sys.argv[1])

def pitchconv(pitch):
	return int(round(1193180.0 / (2**((pitch-69)/12.0)*440), 0))

with open(sys.argv[2], "wb") as out:
	d = 0
	for event in pattern.tracks[1]:
		if event.type == "note_on":
			if event.velocity == 0:
				d += int(round(event.time/48.0, 0))
				p = pitchconv(event.note)
				out.write(bytes([p & 0xff]) + bytes([d << 5 | p >> 8]))
			else:
				d = int(round(event.time/48.0, 0))