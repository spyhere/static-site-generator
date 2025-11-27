from __future__ import annotations


class HTMLNode():
    def __init__(self, tag: str|None = None, value: str|None = None, children: list[HTMLNode]|None = None, props: dict|None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        res = ""
        for key, value in (self.props or {}).items():
            res += f' {key}="{value}"'
        return res

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

