# check if the return of the method has a length greater than 0

from bbquote.get_quote import get_quote
def test_get_quote():
  assert len(get_quote()) > 0