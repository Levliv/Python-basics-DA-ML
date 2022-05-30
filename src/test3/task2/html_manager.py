from contextlib import contextmanager


class HTML:
    def __init__(self):
        self.source: str = ""
        self.number_of_indents: int = 0

    def write(self, text):
        self.source += "  " * self.number_of_indents + text + "\n"

    def div(self):
        return HtmlTag(self, "div")

    def p(self, text):
        self.write(text)

    def body(self):
        return HtmlTag(self, "body")

    def generate(self, filename="test.txt"):
        with open(filename, "w") as file:
            file.write(self.source)

    def increment(self):
        self.number_of_indents += 1

    def decrement(self):
        self.number_of_indents -= 1


class HtmlTag:
    def __init__(self, tag_owner, tag_name):
        self.tag_owner = tag_owner
        self.tag_name = tag_name

    def __enter__(self):
        self.tag_owner.write(f"<{self.tag_name.lower()}>")
        self.tag_owner.increment()

    def __exit__(self, *exc_info):
        self.tag_owner.decrement()
        self.tag_owner.write(f"</{self.tag_name.lower()}>")
