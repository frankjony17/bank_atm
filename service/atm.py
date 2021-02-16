from bank_note import Note

class ATMService:

  def __init__(self, cash: int = 0):
    self.cash = cash
    self.bank_notes = list()

  def get_total_note(self, bank_note: Note):
    remaining_money = self.cash

    if bank_note != None and self.cash >= bank_note.get_note_type():
      bank_note.required_note = self.cash / bank_note.get_note_type()
      remaining_money = self.cash % bank_note.get_note_type()

      if remaining_money == 1 or remaining_money == 3:
        bank_note.required_note -= 1
        remaining_money += bank_note.get_note_type()
      
      self.has_note(bank_note, remaining_money)

  def has_note(self, bank_note: Note, remaining_money: int):
    if bank_note.required_note > 0:
      if bank_note.get_note_count() >= bank_note.required_note:
        bank_note.set_note_count(bank_note.get_note_count() - bank_note.required_note)
      else:
        remaining_money += bank_note.get_note_type() * (bank_note.required_note - bank_note.get_note_count())
        bank_note.required_note = bank_note.get_note_count()
      self.bank_notes.append(bank_note)
    
    self.cash = remaining_money

  def print_cash(self):
    if self.cash == 0:
      print("O valor do saque pode ser expresso em: ")

      for note in self.bank_notes:
        print(f"{int(note.required_note)} notas de {note.get_note_type()}")
    else:
      print("A caixa não tem dinheiro suficiente para o serviço solicitado!!!")
