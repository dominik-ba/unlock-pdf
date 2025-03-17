#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 04.03.2025

@author: Dominik Bartsch
"""

import os

import argparse
import pikepdf

def rotate_right(filename):
    with pikepdf.open(filename, allow_overwriting_input=True) as pdf:
        for page in pdf.pages:
            page.Rotate = (page.Rotate + 90) % 360
        pdf.save(filename)
    print(f"rotated {filename} 90° to the right")

def rotate_left(filename):
    with pikepdf.open(filename, allow_overwriting_input=True) as pdf:
        for page in pdf.pages:
            page.Rotate = (page.Rotate + 270) % 360
        pdf.save(filename)
    print(f"rotated {filename} 90° to the left")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="providing the file name")
    parser.add_argument('-f', '--file_path', type=str, help='path to the encrypted filename')
    parser.add_argument('-d', '--direction', type=str, help='path to the encrypted filename')

    args = parser.parse_args()
    if args.direction.lower() == "right":
        rotate_right(filename=args.file_path)
    elif args.direction.lower() == "left":
        rotate_left(filename=args.file_path)
