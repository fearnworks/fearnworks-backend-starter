from dash import html
import lorem

class PageUtils:
        
    def create_text_block(self, header_text: str, num_paragraphs: int) -> html.Div:
            """
            Creates a text block with a header and one or more paragraphs of lorem ipsum text.

            Args:
                header_text (str): The text to use as the header for the text block.
                num_paragraphs (int): The number of paragraphs of lorem ipsum text to include in the block.

            Returns:
                html.Div: A Div element containing the header and paragraphs of text.
            """
            return html.Div(
                [
                    html.H6(header_text, className="page-1h"),
                    html.P(lorem.paragraph() * num_paragraphs),
                ],
                className="page-1k",
            )
