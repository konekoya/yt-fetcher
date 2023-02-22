import argparse

from yaspin import yaspin
from yaspin.spinners import Spinners

from services import fetch_comments

# Test video ID: '0sOvCWFmrtA'
parser = argparse.ArgumentParser(
    description='Process some integers.', prog="yt-fc")
parser.add_argument('id', type=str, nargs='?', default=None,
                    help='a YouTube video ID')

args = parser.parse_args()
video_id = args.id

if video_id is None:
    print("You didn't specify a YouTube video ID!")
    print()
    parser.print_help()
else:
    loading_text = f"fetching the comments for {video_id}, this may take a while..."
    with yaspin(Spinners.clock, text=loading_text) as sp:
        comments = fetch_comments(video_id)

        # Print out all comments for the video
        index = 0
        for comment in comments:
            index += 1
            print(f'{index}: {comment}')
