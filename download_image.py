#!/auto/releng/bin/ipython
import sys
import requests

try:
    file_name = sys.argv[1]
    #open input file in read mode
    with open(file_name,'r') as f1:
        f = f1.readlines()
    lines = [line.strip() for line in f]

    for line in lines:
        #send request to server and save response
        img  = requests.get(line)
        line = line.rstrip('/')
        downloaded_file  = line.split('/')[-1]
        with open(downloaded_file, 'wb') as im:
            im.write(img.content)
            print('{0} downloaded.\n'.format(downloaded_file))

except Exception as e:
    print('Oops..!!! one or more files could not be downloaded. ERRRRROR --> {0}\n'.format(e))

else:
    print('All files downloaded Successfully...\n')
