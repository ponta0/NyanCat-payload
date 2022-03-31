build:
	cd Data/Image && python2 png2bin.py frames/*.png image.bin
	cd Data/Song && python2 midi2bin.py nyan.mid song.bin
	cd Data && cat Image/image.bin Song/song.bin Other/message.txt > data.bin
	cd Data/Compressor && sed -i -e 's/system("pause");//' compress.c && gcc -o compress compress.c
	cd Data && Compressor/compress data.bin compressed.bin
	nasm -o disk.img kernel.asm
run:
	qemu-system-i386 -s -soundhw pcspk -fda disk.img
clean:
	rm Data/Image/image.bin Data/Song/song.bin Data/data.bin Data/Compressor/compress Data/compressed.bin disk.img
