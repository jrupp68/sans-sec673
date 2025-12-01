import sys
import codecs

def base64_encode(data):
    return codecs.encode(data.encode(),"base64").decode()

def base64_decode(data):
    return codecs.decode(data.encode(), "base64").decode()


if __name__ == "__main__":
    cli_data = " ".join(sys.argv[1:])
    try:
        print(base64_decode(cli_data))
    except:
        print(base64_encode(cli_data))