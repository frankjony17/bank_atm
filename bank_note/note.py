class Note:

  def __init__(self):
    self.__noteType = 0
    self.__noteLimit = 100
    self.__noteCount = 100
    self.requiredNote

    def set_note_type(self, note_type: int):
      self.__note_type = note_type

    def set_note_limit(self, note_limit: int):
      self.__note_limit = note_limit

    def set_note_count(self, note_count: int):
      self.__note_count = note_count

    def get_note_type(self):
      return self.__note_type

    def get_note_limit(self):
      return self.__note_limit

    def get_note_count(self):
      return self.note_count
