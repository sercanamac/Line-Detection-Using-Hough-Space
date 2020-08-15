from LineExtractor import *
import sys
if __name__ == "__main__":
    try:
        source_path = sys.argv[1]
        seg_path = sys.argv[2]
        Extractor = ExtractLines(seg_path,source_path)
        Extractor.start()
    except Exception as e:
        print(e)
        print("Wrong number of arguments")
