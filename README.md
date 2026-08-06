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
To install the source code:
1. Clone the repository at <https://github.com/WhenLifeHandsYouLemons/MagicBook.git>.
2. Install the following packages in `apt`:
```bash
sudo apt update
sudo apt upgrade
sudo apt install swig build-essential python3-dev python3-setuptools liblgpio-dev
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

## License
This project was made by Sooraj S and provided for free for anyone to use, modify, and distribute (given it's also under the same license). To know more about the license, please see the LICENSE.md file.
