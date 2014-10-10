import response
import sys

def search(value):
    for result in response.responses(value):
        print result.name, result.price.value, result.price.currency
        
if __name__ == "__main__":
    search(sys.argv[1])
