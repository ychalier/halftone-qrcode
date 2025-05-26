import argparse
import os
from pathlib import Path

import cv2
import numpy
import qrcode
import qrcode.constants


PATTERNS = [
    [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
    [
        [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]],
    ],
    [
        [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 1, 0], [1, 0, 0]],
        [[0, 0, 1], [0, 1, 0], [0, 0, 1]],
        [[1, 0, 1], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [1, 0, 1]],
    ],
    [
        [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[1, 0, 1], [0, 1, 0], [1, 0, 0]],
        [[0, 0, 1], [1, 1, 0], [1, 0, 0]],
        [[0, 1, 1], [0, 1, 0], [1, 0, 0]],
        [[0, 0, 1], [0, 1, 0], [1, 0, 1]],
        [[0, 0, 1], [0, 1, 0], [1, 1, 0]],
        [[0, 0, 1], [0, 1, 1], [1, 0, 0]],
    ],
    [
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        [[1, 0, 0], [0, 0, 1], [1, 0, 1]],
        [[1, 0, 1], [0, 0, 0], [0, 1, 1]],
        [[1, 0, 0], [0, 0, 1], [0, 1, 1]],
        [[0, 0, 1], [1, 0, 0], [1, 0, 1]],
        [[1, 0, 1], [0, 0, 0], [1, 1, 0]],
        [[0, 0, 1], [1, 0, 0], [1, 1, 0]],
        [[0, 1, 1], [0, 0, 0], [1, 0, 1]],
        [[1, 0, 1], [0, 0, 1], [1, 0, 0]],
        [[0, 1, 1], [0, 0, 1], [1, 0, 0]],
        [[0, 1, 0], [1, 0, 0], [1, 0, 1]],
        [[0, 1, 1], [1, 0, 0], [0, 0, 1]],
        [[1, 1, 0], [1, 0, 0], [0, 0, 1]],
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
        [[1, 0, 0], [1, 0, 1], [0, 1, 0]],
        [[0, 0, 1], [1, 0, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 0, 1], [1, 0, 0]],
        [[0, 1, 0], [1, 0, 1], [0, 0, 1]],
        [[0, 1, 0], [0, 0, 1], [1, 1, 0]],
        [[1, 1, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 0, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 0, 0], [0, 1, 0]],
        [[1, 1, 1], [0, 0, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 0, 0], [1, 1, 1]],
        [[1, 0, 0], [1, 0, 1], [1, 0, 0]],
        [[0, 0, 1], [1, 0, 1], [0, 0, 1]],
        [[1, 1, 0], [0, 0, 0], [0, 1, 1]],
        [[1, 1, 0], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 1], [1, 0, 1], [1, 0, 0]],
        [[0, 0, 1], [0, 0, 1], [1, 1, 0]],
    ],
    [
        [[1, 1, 1], [0, 0, 0], [1, 0, 1]],
        [[1, 1, 1], [0, 0, 0], [0, 1, 1]],
        [[1, 1, 1], [0, 0, 0], [1, 1, 0]],
        [[1, 0, 0], [1, 0, 1], [1, 0, 1]],
        [[1, 0, 1], [1, 0, 0], [1, 0, 1]],
        [[1, 0, 1], [1, 0, 1], [1, 0, 0]],
        [[0, 0, 1], [1, 0, 1], [1, 0, 1]],
        [[1, 0, 1], [0, 0, 1], [1, 0, 1]],
        [[1, 0, 1], [1, 0, 1], [0, 0, 1]],
        [[0, 1, 0], [1, 0, 1], [0, 1, 1]],
        [[1, 1, 0], [0, 0, 1], [0, 1, 1]],
        [[1, 0, 0], [1, 0, 1], [0, 1, 1]],
        [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
        [[1, 1, 0], [1, 0, 1], [0, 0, 1]],
        [[1, 1, 0], [1, 0, 0], [0, 1, 1]],
    ],
    [
        [[1, 1, 1], [0, 0, 0], [1, 1, 1]],
        [[1, 0, 1], [1, 0, 1], [1, 0, 1]],
        [[1, 1, 0], [1, 0, 1], [0, 1, 1]],
        [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
        [[0, 1, 1], [1, 0, 1], [0, 1, 1]],
        [[1, 1, 0], [1, 0, 1], [1, 1, 0]],
        [[0, 1, 0], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [0, 1, 0]],
    ],
    [
        [[1, 1, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 0, 1]],
        [[1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [0, 1, 1]],
        [[1, 1, 0], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 0]],
    ],
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]],
]


class HalftoneQrCode():

    def __init__(self, text: str, input_path: Path, output_path: Path, width: int = 37, mask_path: Path = Path("mask.png"), border_width: int = 12):
        assert width <= 37, "QR Code Width can not be greater than 37"
        self.text = text
        self.input_path = input_path
        self.output_path = output_path
        self.width = width
        self.mask_path = mask_path
        self.border_width = border_width

    @staticmethod
    def make_qrcode(link: str):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=0
        )
        qr.add_data(link)
        qr.make(fit=True)
        return qr.make_image(fill_color="black", back_color="white")

    @staticmethod
    def best_score(halftone: cv2.typing.MatLike, x: int, y: int, tone: int = 8):
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        lowest_diff = None
        lowest_index = 0
        for i in range(len(PATTERNS[tone])):
            vals_patterns = numpy.array([
                PATTERNS[tone][i][0][0],
                PATTERNS[tone][i][0][1],
                PATTERNS[tone][i][0][2],
                PATTERNS[tone][i][1][0],
                PATTERNS[tone][i][1][2],
                PATTERNS[tone][i][2][0],
                PATTERNS[tone][i][2][1],
                PATTERNS[tone][i][2][2],
            ], dtype=numpy.int32)
            vals_image = numpy.array([
                halftone[x-1][y-1],
                halftone[x-1][y],
                halftone[x-1][y+1],
                halftone[x-1][y-1],
                halftone[x-1][y+1],
                halftone[x-1][y-1],
                halftone[x-1][y],
                halftone[x-1][y+1]
            ], dtype=numpy.int32)
            difference = numpy.sum(numpy.abs(vals_patterns * 255 - vals_image))
            if lowest_diff is None or difference <= lowest_diff:
                lowest_diff = difference
                lowest_index = i
        assert lowest_diff is not None
        return lowest_index

    def run(self):
        raw_qrcode = self.make_qrcode(self.text)
        tmp_path = Path("tmp.png")
        with tmp_path.open("wb") as file:
            raw_qrcode.save(file)
        raw_qrcode = cv2.imread(tmp_path.as_posix())
        os.remove(tmp_path)
        if raw_qrcode.shape[0] < 3 * self.width:
            raw_qrcode = cv2.resize(raw_qrcode, (self.width*3, self.width*3), interpolation=cv2.INTER_NEAREST_EXACT)

        assert self.input_path.exists(), f"Input path does not exist {self.input_path}"
        img = cv2.imread(self.input_path.as_posix())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        input_height, input_width = img.shape[:2]
        img_small = cv2.resize(img, (self.width, self.width))
        img_big = cv2.resize(img, (self.width*3, self.width*3))
        for x in range(len(img_big[0])):
            for y in range(len(img_big)):
                img_big[x][y]= -(-float(img_big[x][y]) // 32) * 32 - 1

        halftone = img_big
        for x in range(len(img_small)):
            i = x + 1
            for y in range(len(img_small[0])):
                j = y + 1
                tone = int(img_small[x][y] // 25.5844)
                centerNode = raw_qrcode[i*3-2][j*3-2][0] / 255
                halftone[(i*3-2)][(j*3-2)] = raw_qrcode[(i*3-2)][(j*3-2)][0]
                if tone == 9 and centerNode == 0:
                    tone = 8
                elif centerNode != 0 and tone != 0:
                    tone = tone -1
                elif tone == 0:
                    tone = 0
                patternType = self.best_score(halftone, (i*3-2), (j*3-2), tone)
                halftone[(i*3-2)-1][(j*3-2)-1] = PATTERNS[tone][patternType][0][0] * 255
                halftone[(i*3-2)-1][(j*3-2)]   = PATTERNS[tone][patternType][0][1] * 255
                halftone[(i*3-2)-1][(j*3-2)+1] = PATTERNS[tone][patternType][0][2] * 255
                halftone[(i*3-2)][(j*3-2)-1]   = PATTERNS[tone][patternType][1][0] * 255
                halftone[(i*3-2)][(j*3-2)+1]   = PATTERNS[tone][patternType][1][2] * 255
                halftone[(i*3-2)+1][(j*3-2)-1] = PATTERNS[tone][patternType][2][0] * 255
                halftone[(i*3-2)+1][(j*3-2)]   = PATTERNS[tone][patternType][2][1] * 255
                halftone[(i*3-2)+1][(j*3-2)+1] = PATTERNS[tone][patternType][2][2] * 255

        assert self.mask_path.exists(), f"Mask path does not exist {self.mask_path}"
        mask = cv2.imread(self.mask_path.as_posix())
        if mask.shape[0] < 3 * self.width:
            mask = cv2.resize(mask, (self.width*3, self.width*3), interpolation=cv2.INTER_NEAREST_EXACT)
        for x in range(len(halftone)):
            for y in range(len(halftone[0])):
                if mask[x][y][0] == 255:
                    halftone[x][y]= raw_qrcode[x][y][0]

        halftone = cv2.resize(halftone, (input_width, input_height), interpolation=cv2.INTER_NEAREST_EXACT)
        halftone = cv2.copyMakeBorder(
            halftone,
            self.border_width, self.border_width, self.border_width, self.border_width,
            cv2.BORDER_CONSTANT,
            value=(255,)
        )
        cv2.imwrite(self.output_path.as_posix(), halftone)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="text to embed in the QR Code")
    parser.add_argument("input_path", type=Path, help="source image")
    parser.add_argument("output_path", type=Path, help="output image (PNG)")
    parser.add_argument("-w", "--width", type=int, default=37, help="quantity of white blocks in a box")
    parser.add_argument("-m", "--mask-path", type=Path, default=Path("mask.png"), help="path to control mask")
    args = parser.parse_args()
    HalftoneQrCode(args.text, args.input_path, args.output_path, args.width, args.mask_path).run()


if __name__ == "__main__":
    main()
