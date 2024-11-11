# pysdr-prototyping

### for PULSEAUDIO fm radio through terminal
rtl_fm -f 97.1e6 -M wbfm -s 200000 -r 48000 - | pacat --format=s16le --rate=48000 --channels=1 --latency-msec=100

### for ALSA fm radio through terminal

