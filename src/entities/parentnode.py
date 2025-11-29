from entities.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict | None = None) -> None:
        super().__init__(tag, None, children, props)

    def draw_children_to_html(self) -> str:
        if not self.children:
            raise ValueError(f"No children has been provided for ParentNode {self.tag}")
        res = ""
        for it in self.children:
            res += it.to_html()
        return res

    def to_html(self):
        if not self.tag:
            raise ValueError(f"No tag has been provided for ParentNode {self.tag}")
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
            case "ul":
                return "<ul>" + self.draw_children_to_html() + "</ul>"
            case "ol":
                return "<ol>" + self.draw_children_to_html() + "</ol>"
            case "li":
                return f"<li>{self.draw_children_to_html()}</li>"
            case "pre":
                return f"<pre>{self.draw_children_to_html()}</pre>"
            case _:
                return self.draw_children_to_html()

