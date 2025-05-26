# Halftone QR Code

Implementation of the Halftone QR Code inpired on the original paper by University College London.

## Examples

### Halftone QR Code Embedding

![](examples/river.png)

### Halftone QR Code Video

![](examples/face.gif)

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/) (only for [`embed.py`](embed.py) and [`video.py`](video.py) scripts)

### Installation

1. Clone the repository:
    ```bash
    git clone --recurse-submodules https://github.com/ychalier/halftone-qrcode.git
    cd halftone-qrcode
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    pip install -r fftools/requirements.txt
    ```

### Usage

- Use [`hqr.py`](hqr.py) to generate a halftone QR code from a given text or URL
- Use [`embed.py`](embed.py) to embed a halftone QR code into an image
- Use [`video.py`](video.py) to embed a halftone QR code into a video

For all three scripts, you can run them with the `--help` option to see available options.

## Built With

Original code adapted from [ldpalves/halftoneQrcode](https://github.com/ldpalves/halftoneQrcode), which is based on the paper by University College London: Chu, H. K., Chang, C. S., Lee, R. R., & Mitra, N. J. (2013). Halftone QR codes. ACM transactions on graphics (TOG), 32(6), 1-8.

- [OpenCV](https://opencv.org/) - Computer vision library
- [NumPy](https://numpy.org/) - Numerical computing library
- [qrcode](https://pypi.org/project/qrcode/) - QR code generation library
- [FFtools](https://github.com/ychalier/fftools/) - Video processing tools
