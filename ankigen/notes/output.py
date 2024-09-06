from typing import Iterable

from ankigen.notes.abstractions import NoteABC


def get_lines(notes: Iterable[NoteABC]) -> Iterable[str]:
    yield '#separator:tab\n'
    yield '#tags column:43\n'
    for note in notes:
        yield '\t'.join(note.get_properties()) + '\n'


def write_notes_to_path(filename: str, notes: Iterable[NoteABC]):
    with open(filename, 'w') as f:
        f.writelines(get_lines(notes))