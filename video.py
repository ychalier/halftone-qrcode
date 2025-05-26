"""Create a halftone video QR code.
"""
import argparse
import shutil
from pathlib import Path
import subprocess

import tqdm

from hqr import HalftoneQrCode

import sys
sys.path.insert(0, "./fftools/fftools/")
from fftools.fftools.tools import Resize, Merge


def video(
        input_path: Path,
        width: int,
        height: int,
        qr_text: str,
        output_path: Path,
        fps: str,
        upscale: float = 1,
        border_width: int = 6,
        fit: str = "cover"):
    tmp_dir = Path("tmp")
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir()

    print("Resizing video")
    path_vid = tmp_dir / input_path.name
    Resize.run(argparse.Namespace(input_path=input_path.as_posix(), output_path=path_vid.as_posix(), width=width, height=height, fit=fit, overwrite=True, no_execute=True))

    print("Extracting frames")
    frames_dir = tmp_dir / "frames"
    frames_dir.mkdir()
    subprocess.run(["ffmpeg", "-i", path_vid.as_posix(), (frames_dir / "%09d.png").as_posix()])

    codes_dir = tmp_dir / "codes"
    codes_dir.mkdir()
    for path in tqdm.tqdm(list(frames_dir.glob("*.png")), desc="Generating QR Codes"):
        HalftoneQrCode(qr_text, path, codes_dir / path.name, border_width=border_width).run()

    print("Upscaling")
    upscale_dir = tmp_dir / "upscale"
    upscale_dir.mkdir()
    Resize.run(argparse.Namespace(
        input_path=(codes_dir / "*.png").as_posix(),
        output_path=(upscale_dir / "{stem}.png").as_posix(),
        scale=upscale,
        filter="neighbor",
        overwrite=True,
        no_execute=True,
        global_progress=True))

    print("Merging frames")
    Merge.run(argparse.Namespace(
        input_paths=[(upscale_dir / "*.png").as_posix()],
        output_path=output_path.as_posix(),
        target=str(fps)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=Path, help="input image")
    parser.add_argument("width", type=int, help="output width")
    parser.add_argument("height", type=int, help="output height")
    parser.add_argument("qr_text", type=str, help="QR code text (or URL)")
    parser.add_argument("output_path", type=Path, help="output video")
    parser.add_argument("fps", type=str, help="output video framerate")
    parser.add_argument("-u", "--upscale", type=float, default=1, help="output scaling factor")
    parser.add_argument("-b", "--border-width", type=int, default=1, help="width of white border around QR code")
    parser.add_argument("-f", "--fit", type=str, choices=["fill", "cover", "contain"])
    args = parser.parse_args()
    video(args.input_path, args.width, args.height, args.qr_text, args.output_path, args.fps, args.upscale, args.border_width, args.fit)


if __name__ == "__main__":
    main()
