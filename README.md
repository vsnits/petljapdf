# PetljaPDF
Ultra small suite to download books from pelja.org library

# Install

Try git clone or download manually
```shell
# e.g
$ git clone git://vsnits/petljapdf
# cd petljapdf
```

# How to

> You need to have Wget and WkhtmlToPdf installed

```shell
 $ python3 loadlinks.py
 # You will be asked for petlja link
 # You can configure links.txt manually
 $ python3 petljapdf.py
 # Note it is quite slow
```
Alternatively copy pust links
#
1) Open browser console on head page of desired book
2) Run js from getlinks.js, it will print the links of the book pages
3) Create file links.txt in the current directory e.g "petljapdf/links.txt"
4) Pust links in the created file, you can edit list and choose desired pages
5) Run python, which will download pages and convert to PDF document
```shell
  $ python3 petljapdf.py
```

# License
This code created to get offline study book from petlja.org <br>
It comes with absolutely no Warranty (The Unlicense)
