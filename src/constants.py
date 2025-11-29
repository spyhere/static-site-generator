# ![some alt text](http://localhost:3000) -> ["some alt text", "http://localhost:300"]
MD_IMAGE_GROUPED_REGEXP = r"!\[(.*?)\]\((.*?)\)"

# ![alt text](http://localhost:3000) -> "![alt text](http://localhost:3000)"
MD_IMAGE_ALL_REGEXP = r"!\[.*?\]\(.*?\)"

# [some link](http://localhost:3000) -> ["some link", "http://localhost:3000"]
MD_LINK_GROUPED_REGEXP = r"(?<!!)\[(.*?)\]\((.*?)\)"

# [some link](http://localhost:3000) -> "[some link](http://localhost:3000)"
MD_LINK_ALL_REGEXP = r"(?<!!)\[.*?\]\(.*?\)"

# # Title of Document -> "Title of Document"
MD_TITLE_REGEXP = r"(# )(.*)"

