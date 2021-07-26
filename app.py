import streamlit as st

from bbquote.get_quote import get_quote

quote = get_quote()  # assuming the function returns an author and a quote

f"{quote}"