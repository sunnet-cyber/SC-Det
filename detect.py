# import argparse
import os
import opencc
import codecs

converter = opencc.OpenCC('s2t.json')

def detect(path):
    if os.path.isdir(path):
        for root, dirs, filenames in os.walk(path):
            for file in filenames:
                print('file = ', os.path.join(root, file))
                with open(os.path.join(root, file), mode='rb') as f:
                    for num, line in enumerate(f, 1):
                        line = line.decode("utf-8", 'ignore')
                        if not converter.convert(line) == line:
                            yield "{} {} {}".format(f.name, num, line)
                f.close()

    elif os.path.isfile(path):
        with open(path, mode='rb') as f:
            for num, line in enumerate(f, 1):
                line = line.decode('utf-8', 'ignore')
                if not converter.convert(line) == line:
                    yield "{} {} {}".format(f.name, num, line)
        f.close()


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="SC-Detection.")
#
#     parser.add_argument("--dir", required=True,
#                         help="Path to the files to be scanned")
#
#     main(parser.parse_args())