# Magic Book
## About
This project was made for the Washington renfaire that I went to in *August 2026*.

## Resources
This project used the following hardware:
1. Raspberry Pi 3B
2. Type of LED strip lighting
3. 10,000 mAh power bank
4. Male-to-female, male-to-male, and female-to-female cables
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
6. Once you've completed the hardware setup, simply run the program with:
```
python magic_book.py
```

## Hardware Setup
Just connect the data pin of the LED strip to data pin `18` (in the code this is written as `board.D18`), connect the power and ground pins either to the Raspberry Pi's power and ground pins, or connect them to an external power source!

## License
This project was made by [**Sooraj S**](https://sooraj.dev) and provided for free for anyone to use, modify, and distribute (given it's also under the same license). To know more about the license, please see the [LICENSE](LICENSE) file.
