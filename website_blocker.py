import argparse
import colorama
import os

colorama.init()

# Coloring System

R = "\x1b[30;41;1m"
Y = "\x1b[43;1m"
G = "\x1b[42;1m"

r = "\x1b[31;1m"
g = "\x1b[92;1m"
y = "\x1b[33;1m"

N = "\x1b[0m"


host_file = f"{os.environ['SYSTEMROOT']}\\system32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"

def block(website):
    with open(host_file, "ab+") as file:
        content = file.read()
        
        if website.encode() in content:
            print(f"{R} * {Y} Alert!{N}")
            print(f"{r}{website}{N} has been blocked...")
            pass

        else:
            file.write(f"\n{redirect} {website}".encode())
            print(f"{R} * {G} SUCCESS!{N}")
            print(f"{g}{website}{N} is successfully blocked...")

def unblock(website):
    with open(host_file, "rb+") as file:
        list_web = file.read()

        if website.encode() in list_web:
            new_content = list_web.replace(website.encode(), b" ") # type: ignore
            file.truncate(0)

            file.write(new_content)

            print(f"{R} * {G} SUCCESS!{N}")
            print(f"{g}{website}{N} unblocked succesfully...!")

        else:
            print(f"{R} * {Y} Alert!{N}")
            print(f"{r}{website}{N} has been unblocked...")
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A Simple python website blocker to block and unblock website")
    
    parser.add_argument("-b", "--block", action="store_true", dest="is_block", help="Block a website", default=True)
    parser.add_argument("-x", "--unblock", action="store_false", dest="is_block", help="Unblock a website", default=False)
    parser.add_argument("-u", "--url", dest="url", help="The desired URL to block or unblock", required=True, type=str)

    args = parser.parse_args()

    if args.is_block:
        block(args.url)
    else:
        unblock(args.url)