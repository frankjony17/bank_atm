
from bank_note import Note, note_type
from service.atm import ATMService

note_2_reais = Note()
note_2_reais.set_note_type(2)
note_2_reais.set_note_limit(100)
note_2_reais.set_note_count(100)

cash = input("Informe o valor do saque (valor inteiro): ")

atm = ATMService(int(cash))

for note in note_type.NoteType:
  note_x_reais = note_2_reais.clone()
  note_x_reais.set_note_type(note.get_value())
  atm.get_total_note(note_x_reais)

atm.get_total_note(note_2_reais)

atm.print_cash()