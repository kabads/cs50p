import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    search = re.compile(r'<iframe[^>]+src="(http(s)?://(www.)?youtube\.com/embed/[a-zA-Z0-9_-]+)')
    match = search.search(s)
    if match:
        url= match.group(1)
        id_search = re.compile(r"youtube\.com/embed/([a-zA-Z0-9_-]+)")
        id_match = id_search.search(url)
        if id_match:
            new_url = "https://youtu.be/" + id_match.group(1)
            return new_url
    else:
        return None


if __name__ == "__main__":
    main()

# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>