import utils.image as image
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--extract',type=bool,default=False)
arg_parser.add_argument('--video',type=str,default='./')
arg_parser.add_argument('--saved',type=str,default='./')
arg_parser.add_argument('--every',type=int,default=1)
arg_parser.add_argument('--max',type=int,default=0)
arg_parser.add_argument('--prefix',type=str,default='')
args = arg_parser.parse_args()


def main():
    if args.extract:
        image.video2images(video_file=args.video,saved_path=args.saved,every_frames=args.every,max_frames=args.max,prefix=args.prefix)
    pass



if __name__ == '__main__':
    main()


