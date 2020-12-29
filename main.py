import JSONTools
import DBTools
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Piotrek - update on github')
    print_hi('second line printed')
    print_hi('forth lone printed new commit to exist pull request')
    print_hi('fifth - to check if new commit will be pull from different branch than master')
    jsonObj = JSONTools.Json()
    jsonObj.getJson()
    data = jsonObj.getDataFromJson()
    dataString = json.dumps(data)
    productsList = json.loads(dataString, object_hook=JSONTools. productJsonDecod)

    db = DBTools.DB()
    db.dbInsertProducts(productsList)
