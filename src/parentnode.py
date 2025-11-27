from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict | None = None) -> None:
        super().__init__(tag, None, children, props)

    def draw_children_to_html(self):
        if not self.children:
            raise ValueError("No children has been provided for ParentNode")
        res = ""
        for it in self.children:
            res += it.to_html()
        return res

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag has been provided for ParentNode")
        match self.tag:
            case "p":
                return f"<p>{self.draw_children_to_html()}</p>"
            case "a":
                return f"<a{self.props_to_html()}>{self.draw_children_to_html()}</a>"
            case "b":
                return f"<b>{self.draw_children_to_html()}</b>"
            case "i":
                return f"<i>{self.draw_children_to_html()}</i>"
            case "span":
                return f"<span>{self.draw_children_to_html()}</span>"
            case "div":
                return f"<div>{self.draw_children_to_html()}</div>"
            case _:
                return self.draw_children_to_html()

