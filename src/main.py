from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is supposed to be bold", TextType.BOLD)
    print(node)

    html_node = HTMLNode(tag="p", value="This is supposed to be an html node")
    print(html_node)

if __name__ == "__main__":
    main()