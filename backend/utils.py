import csv
import json

def textfile_to_var(filename_withpath, return_datatype):
    filecontent_txt = ""
    with open(filename_withpath, 'r') as file:
        filecontent_txt = file.read()

    if return_datatype == "json":
        returnvariable = json.loads(filecontent_txt)
    elif return_datatype == "string":
        returnvariable = filecontent_txt
    else:
        returnvariable = filecontent_txt

    return returnvariable