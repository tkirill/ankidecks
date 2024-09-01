from data.gerund_or_infinitive import read_gerund_or_infinitive_data
from notes import write_notes_to_path
from notes.basic_example import BasicExampleNote
from concordance import skell


def generate_gerunds_or_infinitive():
    data = read_gerund_or_infinitive_data('./data/gerund_or_infinitive.json')
    notes = []
    for key, item in data.items():
        for followed_by in item.followed_by:
            examples = skell.get_examples(f'{key} .*?ing')
            note = BasicExampleNote(key, followed_by, examples)
            notes.append(note)
    write_notes_to_path('gerund_or_infinitive.txt', notes)