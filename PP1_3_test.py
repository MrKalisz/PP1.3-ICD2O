import os.path
import sys
from PP1_3 import *

def test_q1(capsys):

  try:
    exists = os.path.exists("PP1_3.py")
    assert exists
  except:
    sys.exit()

  q1()
  captured = capsys.readouterr()
  assert captured.out == "* * * * *\n * * * * *\n* * * * *\n * * * * *\n* * * * *\n\n* * * *\n*     *\n*     *\n*     *\n* * * *\n\n* * * * *\n *     *\n  *   *\n   * *\n    *"

def test_q2(capsys):

  try:
    exists = os.path.exists("PP1_3.py")
    assert exists
  except:
    sys.exit()

  q2()
  captured = capsys.readouterr()
  assert captured.out == "Hello World"

def test_q3(capsys):

  try:
    exists = os.path.exists("PP1_3.py")
    assert exists
  except:
    sys.exit()

  q3()
  captured = capsys.readouterr()
  assert captured.out == '"Man"\n"Board"\n"Man Overboard"\n'

