import json
import xml.dom.minidom as MD
dom=MD.Document()

def addxml(tagname,data):

    if type(data) is dict:
        for i in data:
            child= dom.createElement(i)
            tagname.appendChild(child)
            addxml(child,data=data[i])
    elif type(data) is list:
        for i in data:
            child= dom.createElement(tagname.tagName)
            tagname.appendChild(child)
            addxml(tagname=child,data=i)
    else:
        child=dom.createTextNode(data=str(data))
        tagname.appendChild(child)
    return tagname

def display_element(element,indext=0):
    print(" "*indext+"<"+element.tagName+'>')
    for child in element.childNodes:
        if child.nodeType==child.ELEMENT_NODE:
            display_element(child,indext+2)
        elif child.nodeType== child.TEXT_NODE:
            print(' '*(indext+2)+child.nodeValue)
    print(" "*indext+"</"+element.tagName+'>')

if __name__=='__main__':
    with open('outjson.json','r') as file:
        data=json.load(fp=file)
    print(type(data))
    child=dom.createElement('root')
    dom.appendChild(child)

    xmldata=addxml(child,data=data)
    print(xmldata.childNodes)
    display_element(child)
    with open('outxml1.xml','w') as file:
        file.write(dom.toxml())


