import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    matches = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]{11})', s)
    if matches:
        code_video = matches.group(1)
        return "https://youtu.be/"+matches.group(1)
    else:
        return None

if __name__ == "__main__":
    main()
