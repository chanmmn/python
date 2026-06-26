#!/usr/bin/env python3
"""Trim zhang.mp4 to the first 3 minutes 40 seconds and save to a new file."""

import subprocess
import sys

import imageio_ffmpeg

INPUT_FILE = "zhang.mp4"
OUTPUT_FILE = "zhang_trimmed.mp4"
DURATION_SECONDS = 4 * 60 + 10  # 3 minutes 40 seconds


def main() -> int:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg,
        "-y",
        "-i", INPUT_FILE,
        "-t", str(DURATION_SECONDS),
        "-c", "copy",
        OUTPUT_FILE,
    ]
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode == 0:
        print(f"Saved first {DURATION_SECONDS}s to {OUTPUT_FILE}")
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
