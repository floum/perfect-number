from perfect_number import perfect_number

def test_perfect_number():
  assert perfect_number(6)
  assert not perfect_number(5)
  assert perfect_number(28)
