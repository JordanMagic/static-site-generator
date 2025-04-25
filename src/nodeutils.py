from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD | TextType.ITALIC | TextType.CODE:
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.LINK:
            return LeafNode(TextType.LINK.value, text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(TextType.IMAGE.value, "", props={"src": text_node.url, "alt": text_node.text})
