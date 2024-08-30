#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30.08.2024

@author: Dominik Bartsch
"""

import os
import argparse
import PyPDF2


def merge_pdfs(pdf_list, output):
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        pdf_merger.append(pdf)
    
    with open(output, 'wb') as f:
        pdf_merger.write(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="providing the file names")
    parser.add_argument('-1', '--file_one', type=str, help='path to the first pdf file')
    parser.add_argument('-2', '--file_two', type=str, help='path to the second pdf file')
    
    args = parser.parse_args()
    
    pdfs = [args.file_one, args.file_two]
    merge_pdfs(pdfs, 'merged.pdf')
