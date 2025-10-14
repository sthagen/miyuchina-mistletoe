"""
Make mistletoe easier to import.
"""

__version__ = "1.5.0.dev"
__all__ = ['html_renderer', 'ast_renderer', 'block_token', 'block_tokenizer',
           'span_token', 'span_tokenizer']

from typing import Callable, Iterable, Union

from mistletoe.base_renderer import BaseRenderer
from mistletoe.block_token import Document
from mistletoe.html_renderer import HtmlRenderer
# import the old name for backwards compatibility:
from mistletoe.html_renderer import HTMLRenderer  # noqa: F401


def markdown(iterable: Union[str, Iterable[str]], renderer: Callable[..., BaseRenderer] = HtmlRenderer):
    """
    Converts markdown input to the output supported by the given renderer.
    If no renderer is supplied, ``HtmlRenderer`` is used.

    Note that extra token types supported by the given renderer
    are automatically (and temporarily) added to the parsing process.
    """
    with renderer() as r:
        return r.render(Document(iterable))
