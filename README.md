# Image converter
A simple image converter using python.
Size and format of an image can be converted using this image converter


## Installation

Install pillow using pip.

```sh
pip intall pillow
```

## Usage:
```sh
python resizer.py [input file name] [operation] [argument]

Operation: 
-f : to change format of image
Example 1: python resizer.py image.jpeg -f png 
Example 2: python resizer.py image.png -f jpeg 

-r : To  resize the image
Example 1: python resizer.py image.jpeg -r 200x200 
Example 2: python resizer.py image.jpeg -r 250x200 
```


## Examples:
1. Image format conversion

```sh
python resizer.py image.jpeg -f png 
```

2. Image resizing
```sh
python resizer.py image.jpeg -r 200x200 
```

## Libraries used:

- [Pillow](https://python-pillow.org/)
