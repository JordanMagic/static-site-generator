from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        def recurse_to_html(node):
            if not isinstance(node, ParentNode):
                return node.to_html()

            html = f"<{node.tag}>"
            for child in node.children:
                html += recurse_to_html(child)
            return html + f"</{node.tag}>"

        return recurse_to_html(self)