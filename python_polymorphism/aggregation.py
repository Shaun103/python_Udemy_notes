class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag} {self.contents} {self.end_tag}"

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:            
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)
    
 
class Body(Tag):

    def __init__(self):
        super().__init__('body', '') # body contents will be built up seperately 
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body
    
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


def main():
    print()

    new_body = Body()

    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances of objects to build up another object.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of if it's destroyed, those objects continue to exist.")

    new_body.add_tag('br', " ")
    new_body.add_tag('img src="pixelart.png" alt="Italian Trulli"', " ")

    new_body.add_tag('p', "This is a typing test any mistyakes are going to stay into the document while I am typing on this line ")
    new_body.add_tag('p', "I am testing this line if there is a break withint the program")

    new_docType = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_docType, new_header, new_body)
    
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)


if __name__ == "__main__":
    main()