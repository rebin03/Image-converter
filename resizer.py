from PIL import Image
import sys

try:
    fullimageFileName = sys.argv[1]
  
    operation = sys.argv[2]

    argument = sys.argv[3]

    if operation == '-format':
        
        r = fullimageFileName.split('.')

        imageFileName = r[0]

        im = Image.open(fullimageFileName)

        converted = im.convert('RGB')

        converted.save(f'{imageFileName}out.{argument}')


    elif operation == '-resize':

        im = Image.open(fullimageFileName)

        r = argument.split('x')

        r_tuple = (int(r[0]), int(r[1]))

        out = im.resize(r_tuple)

        out.save(f'New_{fullimageFileName}')

except:
    print('Usage')
    print('python resizer.py [input file name] [operation] [argument]')
    print('Operation: ')
    print('-format :To change format of image')
    print('Example 1: python resizer.py image.jpeg -format png ')
    print('Example 2: python resizer.py image.png -format jpeg ')
    print()
    print('-resize :To resize the image')
    print('Example 1: python resizer.py image.jpeg -resize 200x200 ')
    print('Example 2: python resizer.py image.jpeg -resize 250x200 ')