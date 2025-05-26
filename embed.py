"""Embed a halftone QR code within a larger image (test multiple positions).
"""
import argparse
import math
import shutil
from pathlib import Path

import cv2
import tqdm

from hqr import PATTERNS, HalftoneQrCode

import sys
sys.path.insert(0, "./fftools/fftools/")
from fftools.fftools.tools import Resize, Cut
from fftools.fftools.utils import startfile


def halftone(input_path: Path, output_path: Path):
    raw_qrcode = cv2.cvtColor(cv2.imread(input_path.as_posix()), cv2.COLOR_BGR2GRAY)
    halftone = raw_qrcode
    height = math.ceil(raw_qrcode.shape[1] / 3)
    width = math.ceil(raw_qrcode.shape[0] / 3)
    for x in range(width):
        i = x
        for y in range(height):
            j = y
            tone = int(raw_qrcode[x*3][y*3] // 25.5844)
            centerNode = float(raw_qrcode[i*3-2][j*3-2]) / 255
            halftone[(i*3-2)][(j*3-2)] = int(raw_qrcode[(i*3-2)][(j*3-2)] / 128) * 255
            if tone == 9 and centerNode == 0:
                tone = 8
            elif centerNode != 0 and tone != 0:
                tone = tone -1
            elif tone == 0:
                tone = 0
            patternType = HalftoneQrCode.best_score(halftone, (i*3-2), (j*3-2), tone)
            halftone[(i*3-2)-1][(j*3-2)-1] = PATTERNS[tone][patternType][0][0] * 255
            halftone[(i*3-2)-1][(j*3-2)]   = PATTERNS[tone][patternType][0][1] * 255
            halftone[(i*3-2)-1][(j*3-2)+1] = PATTERNS[tone][patternType][0][2] * 255
            halftone[(i*3-2)][(j*3-2)-1]   = PATTERNS[tone][patternType][1][0] * 255
            halftone[(i*3-2)][(j*3-2)+1]   = PATTERNS[tone][patternType][1][2] * 255
            halftone[(i*3-2)+1][(j*3-2)-1] = PATTERNS[tone][patternType][2][0] * 255
            halftone[(i*3-2)+1][(j*3-2)]   = PATTERNS[tone][patternType][2][1] * 255
            halftone[(i*3-2)+1][(j*3-2)+1] = PATTERNS[tone][patternType][2][2] * 255
    cv2.imwrite(output_path.as_posix(), halftone)


def embed_hqr(input_path: Path, width: int, height: int, qr_text: str, output_dir: Path, upscale: float = 1, border_width: int = 1, fit: str = "cover"):
    tmp_dir = Path("./tmp")
    tmp_dir.mkdir(exist_ok=True)
    path_in = tmp_dir / "in.png"
    path_in_ht = tmp_dir / "in_halftone.png"
    grid_dir = tmp_dir / "grid"
    if grid_dir.exists():
        shutil.rmtree(grid_dir)
    grid_dir.mkdir()
    codes_dir = tmp_dir / "codes"
    if codes_dir.exists():
        shutil.rmtree(codes_dir)
    codes_dir.mkdir()
    variants_dir = tmp_dir / "variants"
    if variants_dir.exists():
        shutil.rmtree(variants_dir)
    variants_dir.mkdir()

    print("Resizing image")
    Resize.run(argparse.Namespace(input_path=input_path.as_posix(), output_path=path_in.as_posix(), width=width, height=height, fit=fit, overwrite=True, no_execute=True))

    print("Halftoning image")
    halftone(path_in, path_in_ht)

    print("Splitting image into grid")
    Cut.run(argparse.Namespace(input_path=path_in.as_posix(), output_path=(grid_dir / "{row}_{col}.png").as_posix(), max_width=111, max_height=111, overwrite=True, no_execute=True))

    for path in tqdm.tqdm(list(grid_dir.glob("*.png")), desc="Generating QR Codes"):
        HalftoneQrCode(qr_text, path, codes_dir / path.name, border_width=border_width).run()

    bg = cv2.imread(path_in_ht.as_posix())
    rows = cols = -1
    for path in list(codes_dir.glob("*.png")):
        i, j = tuple(map(int, path.stem.split("_")))
        rows = max(rows, i)
        cols = max(cols, j)
    rows += 1
    cols += 1
    for path in tqdm.tqdm(list(codes_dir.glob("*.png")), "Generating output variants"):
        code = cv2.imread(path.as_posix())
        img = bg.copy()
        i, j = tuple(map(int, path.stem.split("_")))
        sy = i * 111 - border_width
        sx = j * 111 - border_width
        sh = 111 + 2 * border_width
        sw = 111 + 2 * border_width
        dy = 0
        dx = 0
        if i == 0:
            sy = 0
            dy = border_width
            sh -= border_width
        if j == 0:
            sx = 0
            dx = border_width
            sw -= border_width
        if i == rows - 1:
            sy = height - 111 - border_width
            sh -= border_width
        if j == cols - 1:
            sx = width - 111 - border_width
            sw -= border_width
        img[sy:sy+sh, sx:sx+sw, :] = code[dy:dy+sh, dx:dx+sw, :]
        cv2.imwrite((variants_dir / path.name).as_posix(), img)

    output_dir.mkdir(exist_ok=True)
    for path in tqdm.tqdm(list(codes_dir.glob("*.png")), "Upscaling variants"):
        Resize.run(argparse.Namespace(input_path=(variants_dir / path.name).as_posix(), output_path=(output_dir / path.name).as_posix(), scale=upscale, filter="neighbor", overwrite=True, no_execute=True))

    startfile(output_dir)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=Path, help="input image")
    parser.add_argument("width", type=int, help="output width")
    parser.add_argument("height", type=int, help="output height")
    parser.add_argument("qr_text", type=str, help="QR code text (or URL)")
    parser.add_argument("output_dir", type=Path, help="output directory")
    parser.add_argument("-u", "--upscale", type=float, default=1, help="output scaling factor")
    parser.add_argument("-b", "--border-width", type=int, default=1, help="width of white border around QR code")
    parser.add_argument("-f", "--fit", type=str, choices=["fill", "cover", "contain"])
    args = parser.parse_args()
    embed_hqr(args.input_path, args.width, args.height, args.qr_text, args.output_dir, args.upscale, args.border_width, args.fit)


if __name__ == "__main__":
    main()
