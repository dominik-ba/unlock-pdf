# pdf tools

simple python scripts which help you to do pdf actions without paying for adobe pro or upload your files to the internet.

## usage unlock pdf

To unlock pdfs aka. remove the password.

```bash
pipenv install
pipenv run python unlock-pdf.py -f "path_to_the_encrypted_file.pdf" -p my_super_strong_password1!
```

Decrypted file will be in the same folder as the current execution path, having the the sanme name with a suffix of `-decrypted`

## usage merge pdfs

Merge two pdfs to one. (with small adjustment it can be used for any number of pdf files).

```bash
pipenv install
pipenv run python .\combine-pdf.py -1 "path_to_the_first_file.pdf" _2 "path_to_the_second_file.pdf"
```

Merged file will be in the same folder as the current execution path. Name: `merged.pdf`
