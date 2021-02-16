from enum import Enum

class NoteType(Enum):
  TWO_HUNDRED = 200
  ONE_HUNDRED = 100
  FIFTY = 50
  TWENTY = 20
  TEN = 10
  FIVE = 5

  def get_value(self):
    return self.value