# radio_presets_mp
Python 3: Radio Presets MP (Wrapper): mplayer wrapper, csv.reader(), subprocess.run(), fileObject

## CLI

`mplayer` is a dependency which needs to found on PATH. It is the media player installed in the OS; the secret sauce of the radio streams.

```bash
$ python3 radio_presets_mp.py
```

Press `q` to quit stream.

## CSV Reader

```python
from csv import reader
```

```python
csv_read = reader(file_obj, delimiter=',')
```

```python
>>> file_obj.name
'stations_urls.csv'
>>> file_obj.mode
'r'
>>> file_obj.encoding
'UTF-8'
```

```python
>>> csv_read
<_csv.reader object at 0x7f5ace717278>
>>> csv_read.line_num
36
```

[csv.reader()](https://docs.python.org/3/library/csv.html#csv.reader) reads/parses tabular data in `stations_urls.csv`, and receives `file_obj` as the first argument which stores a [TextIOWrapper](https://docs.python.org/3.8/library/io.html#io.TextIOWrapper) with UTF-8 encoding, followed by a `delimiter` parameter which indicates that the comma will be the field separator in the CSV database.

The value `36` stored in `csv_read.line_num` indicates that `csv_reader()` will read 36 lines, not counting the first header line.

## Subprocess Run

```python
from subprocess import run
```

```python
run(["mplayer", urls[station_num]])
```

`subprocess.run()` receives a list of parameters which become command line arguments passed to the Unix shell. In this case, `mplayer`, followed by a Internet radio station URL.

## Dictionary

```python
urls = {}
```

```python
for rec in csv_read:
    print(f'{c:>2}: {rec[0]}')
    urls[c] = rec[1]
```

The looping structure will insert numerical keys and URL values into the `urls` dictionary: `urls[c] = rec[1]`. The number will be generated by an incremental counter: `urls[c]`. The value will come from the second field of a CSV record: `rec[1]`.

```python
>>> import pprint
>>> pprint.pprint(urls)
{1: 'http://ice2.somafm.com/defcon-128-aac',
 2: 'http://ice1.somafm.com/dronezone-256-mp3',
 3: 'https://somafm.com/deepspaceone130.pls',
 4: 'http://somafm.com/sf1033130.pls',
 5: 'https://somafm.com/missioncontrol130.pls',
 6: 'http://ice3.somafm.com/spacestation-128-mp3',
 7: 'http://somafm.com/specials130.pls',
 8: 'http://176.31.123.212:8192/index.html',
 9: 'http://streams.echoesofbluemars.org:8000/bluemars',
 10: 'http://streams.echoesofbluemars.org:8000/cryosleep',
 11: 'http://s3.viastreaming.net:8835/',
 12: 'http://air.verdure.net:8881/stream',
 13: 'http://ice1.somafm.com/groovesalad-256-mp3',
 14: 'https://somafm.com/gsclassic130.pls',
 15: 'http://systrum.net:8000/Systrum-Channel1.m3u',
 16: 'http://136.243.156.30:1701/stream/2/',
 17: 'http://149.56.234.138:8169/stream',
 18: 'http://7rays.stream.laut.fm/7rays',
 19: 'http://air.radiorecord.ru:8102/chil_320',
 20: 'http://station.waveradio.org/provodach',
 21: 'http://5.189.142.165:2304/stream',
 22: 'http://tachyon.shoutca.st:8919/stream',
 23: 'http://79.111.119.111:8002/droneambient',
 24: 'http://philae.shoutca.st:9019/stream',
 25: 'http://uk1.internet-radio.com:8004/stream',
 26: 'http://198.24.145.146:9318/stream',
 27: 'http://mixlive.ie:9332/;ambient',
 28: 'http://i.20hz.biz:8000/maschinengeist.org.192.mp3',
 29: 'http://aska.ru-hoster.com:8053/autodj',
 30: 'http://46.105.124.120:8604/stream',
 31: 'http://radio.hbr1.com:19800/ambient.ogg',
 32: 'http://108.61.154.147:5940',
 33: 'http://ubuntu.hbr1.com:19800/ambient.ogg',
 34: 'http://radio.stereoscenic.com/asp-s',
 35: 'http://radio.stereoscenic.com/asp-h',
 36: 'http://radio.stereoscenic.com/mod-h'}
```

## Print Header

```python
print(f'{file_obj.readline()}')
```

The `readline()` method call prints one line at a time. So, if the same call repeats, the built-in `__next__` method could print each successive line&mdash;one by one. In this case, it is only used to print the first line, which is typically a header line: `========== Station List [Radio Presets MP] ==========`

## Initialize Counter

```python
c = 1
```

This counter initializes with the number `1` because it is used to number the YouTube URLs, which will allow a user to select a numbered Internet radio station.

```python
c += 1
```

The counter is incremented by `1`.

## Pick Radio Station Number

```python
station_num = int(input('\x1b[1;36mEnter station number\x1b[0m: '))
```

After the radio station list prints, the last line (cyan in color) is where a user inputs their selection number, which is stored in the `station_num` variable:

```bash
Enter station number: 5
```

See _Subprocess Run_ section above.
