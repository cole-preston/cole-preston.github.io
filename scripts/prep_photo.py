#!/usr/bin/env python3
"""Prepare a photo for the website: fix rotation, strip all metadata, resize, compress.

Every photo added to images/ should go through this script first. It removes
EXIF (including GPS location), XMP and ICC data, so nothing about where or with
what device a photo was taken ends up in the repository.

Requires Pillow:  pip install Pillow

Examples:
  # Travel photo: at most 1600px wide (default)
  python3 scripts/prep_photo.py ~/Desktop/IMG_1234.jpeg images/travels/mt-takao.jpg

  # Square avatar: crop a square around a point, then resize to 500x500
  python3 scripts/prep_photo.py headshot.jpeg images/avatar.jpg --square 500 --center 0.5 0.45 --crop-size 0.55
"""

import argparse

from PIL import Image, ImageOps


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("src", help="original photo")
    parser.add_argument("dest", help="output .jpg path")
    parser.add_argument("--max-width", type=int, default=1600, help="max output width in px (default 1600)")
    parser.add_argument("--square", type=int, metavar="PX", help="crop to a square and resize to PX x PX")
    parser.add_argument("--center", type=float, nargs=2, default=(0.5, 0.5), metavar=("X", "Y"),
                        help="square crop center as fractions of width/height (default 0.5 0.5)")
    parser.add_argument("--crop-size", type=float, default=1.0,
                        help="square crop side as a fraction of the shorter edge (default 1.0)")
    parser.add_argument("--quality", type=int, default=82, help="JPEG quality (default 82)")
    args = parser.parse_args()

    img = Image.open(args.src)
    img = ImageOps.exif_transpose(img)  # bake in rotation before the orientation tag is dropped
    img = img.convert("RGB")

    if args.square:
        w, h = img.size
        side = round(min(w, h) * args.crop_size)
        cx, cy = args.center[0] * w, args.center[1] * h
        left = min(max(round(cx - side / 2), 0), w - side)
        top = min(max(round(cy - side / 2), 0), h - side)
        img = img.crop((left, top, left + side, top + side))
        img = img.resize((args.square, args.square), Image.LANCZOS)
    elif img.width > args.max_width:
        new_h = round(img.height * args.max_width / img.width)
        img = img.resize((args.max_width, new_h), Image.LANCZOS)

    # Re-encoding from raw pixels without exif=/icc_profile= writes no metadata at all.
    clean = Image.frombytes("RGB", img.size, img.tobytes())
    clean.save(args.dest, "JPEG", quality=args.quality, optimize=True, progressive=True)
    print(f"wrote {args.dest} ({clean.width}x{clean.height})")


if __name__ == "__main__":
    main()
