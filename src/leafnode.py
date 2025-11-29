from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str|None = None, value: str = "", props: dict | None = None) -> None:
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value in the LeafNode")
        if not self.tag:
            return self.value
        match self.tag:
            case "h1":
                return f"<h1>{self.value}</h1>"
            case "h2":
                return f"<h2>{self.value}</h2>"
            case "h3":
                return f"<h3>{self.value}</h3>"
            case "h4":
                return f"<h4>{self.value}</h4>"
            case "h5":
                return f"<h5>{self.value}</h5>"
            case "h6":
                return f"<h6>{self.value}</h6>"
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
            case "code":
                return f"<code>{self.value}</code>"
            case "quote":
                return f"<quote>{self.value}</quote>"
            case "img":
                return f"<img{self.props_to_html()} />"
            case _:
                return self.value

