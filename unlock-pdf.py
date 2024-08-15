#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 15.08.2024

@author: Dominik Bartsch
"""

import os

import argparse
import pikepdf

def remove_file_extension(filename):
    root, _ = os.path.splitext(filename)
    return root


def remove_password_from_pdf(filename, password=None):
    pdf = pikepdf.open(filename, password=password)
    sourcename = os.path.basename(filename)
    savename = remove_file_extension(sourcename) + "-decrypted.pdf"
    pdf.save(savename)
    print(f"Decrypted {sourcename} and stored new file at {savename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="providing the file name and password")
    parser.add_argument('-f', '--file_path', type=str, help='path to the encrypted filename')
    parser.add_argument('-p', '--password', type=str, default=None, help='the password')
    
    args = parser.parse_args()
    
    remove_password_from_pdf(filename=args.file_path, password=args.password)
