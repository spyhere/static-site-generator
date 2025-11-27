from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict | None = None) -> None:
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value in the LeafNode")
        if not self.tag:
            return self.value
        match self.tag:
            case "p":
                return f"<p>{self.value}</p>"
            case "a":
                return f"<a{self.props_to_html()}>{self.value}</a>"
            case "b":
                return f"<b>{self.value}</b>"
            case "i":
                return f"<i>{self.value}</i>"
            case "span":
                return f"<span>{self.value}</span>"
            case "div":
                return f"<div>{self.value}</div>"
            case _:
                return self.value

