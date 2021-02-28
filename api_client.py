import requests
import os
import json

path = '../../temp/2021-02-28 (copy)'
with os.scandir(path) as entries:
    print("analyse path: " + path)

    try:
        os.mkdir(path + "/cars")
    except:
        pass

    for entry in entries:
        print("analyse image: " + entry.name)
        if entry.is_file():
            if entry.name.endswith('.jpg') or entry.name.endswith('.thumb'):
                file = open(entry, 'rb')
                files={"image": file}
                res=requests.post(url='http://127.0.0.1:6000',
                                  files=files)

                if res.status_code == 200:
                    cars=res.json()['cars']
                    if cars == []:
                        print("no car in file, remove: " + entry.name)
                        os.remove(entry)
                    else:
                        extra_fn = ''
                        for car in cars:
                            extra_fn = extra_fn + "-{}-{}-{}".format(car['make'], car['model'], car['color'])
                        fn_parts = entry.name.split('.')
                        newPath=path + '/cars/' + fn_parts[0] + extra_fn + '.' + fn_parts[1]
                        print("move file to: " + newPath)
                        os.rename(entry.path, newPath)
            else:
                print("no picture, remove: " + entry.name)
                os.remove(entry)




