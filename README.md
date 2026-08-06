# Magic Book
## About
This project was made for the Washington renfaire that I went to in *August 2026*.

## Resources
This project used the following hardware:
1. Raspberry Pi 4B (a Raspberry Pi 3B or lower works just as well, however it requires the LED strip to be powered externally)
2. 1-metre BTF-Lighting WF2812B IC LED Strip (60 LEDs/m)
3. 10,000 mAh power bank
4. Male-to-female, male-to-male, and female-to-female cables (only 3 male-to-female cables were used, but the other might come in handy if soldering work is needed)
5. A thick hard-cover book (preferrably leather-like cover to look more like a spell book)

## Installation
To install the source code and run the program:
1. Install the following packages in `apt`:
```bash
sudo apt update
sudo apt upgrade
sudo apt install git swig build-essential python3-dev python3-setuptools liblgpio-dev
```
2. Clone the repository at <https://github.com/WhenLifeHandsYouLemons/Magic-Book.git> with:
```bash
git clone https://github.com/WhenLifeHandsYouLemons/Magic-Book.git
```
3. Then, create the virtual environment in the project folder:
```bash
cd MagicBook
python -m venv .venv
```
4. Once the virtual environment is installed, activate it with:
```bash
source .venv/bin/activate
```
5. And finally install the PIP packages required for the project with:
```bash
pip install -r requirements.txt
```
6. Once you've completed the hardware setup, run the program with (this is needed instead of simply running `python magic_book.py` as neopixels needs `sudo` to run but we're using a virtual environment):
```
sudo -E env PATH=$PATH python3 magic_book.py
```

## Hardware Setup
Just connect the data pin of the LED strip to GPIO `24` (in the code this is written as `board.D18`), connect the power and ground pins either to the Raspberry Pi's (4B or higher model) power and ground pins, or connect them to an external power source (for a Raspberry Pi 3B or a lower model)!

Raspberry Pi 40-pin GPIO layout:
<img width="2064" height="1185" alt="GPIO Pinout Diagram" src="https://github.com/WhenLifeHandsYouLemons/Magic-Book/blob/main/GPIO-Pinout-Diagram.png" />
(Taken from: <https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio>)

## License
This project was made by [**Sooraj S**](https://sooraj.dev) and provided for free for anyone to use, modify, and distribute (given it's also under the same license). To know more about the license, please see the [LICENSE](LICENSE) file.
