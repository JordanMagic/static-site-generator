from textnode import TextType, TextNode

def main():
    node = TextNode("This is supposed to be bold", TextType.BOLD)
    print(node)

if __name__ == "__main__":
    main()