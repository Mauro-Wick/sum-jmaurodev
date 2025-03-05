def test_sum_total():
  assert sum_total(1,1) == 2
  assert sum_total(1,0) == 1
  assert sum_total(0,1) == 1
  assert sum_total(0,0) == 0
  assert sum_total(-1,-1) == -2
  assert sum_total(-1,1) == 0
  assert sum_total(1,-1) == 0
