import json
import urllib.request, urllib.response, urllib.error


def convertJSONToData( jsonText ):
    return json.loads( jsonText )



webAddress = input( "Enter the web address of the json file you want to convert to a python data structure >>  " )
responseHandle = urllib.request.urlopen( webAddress )
response = ""


for resp in responseHandle:
    response += resp.decode()
    print("data is loading")
else:
    print( "\n" )
    dataFromResponse = convertJSONToData( response )
    print( f"The object returned is of class: { type( dataFromResponse ) }" )
    for ( x, y ) in dataFromResponse.items():
        print( x, tab , y )
