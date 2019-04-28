def file_to_var(filename_withpath, returntype):
    filecontent_txt = ""
    with open(filename_withpath, 'r') as file:
        filecontent_txt = file.read()

    if returntype == "json":
        returnvariable = json.loads(filecontent_txt)
    elif returntype == "text":
        returnvariable = filecontent_txt
    else:
        returnvariable = filecontent_txt

    return returnvariable