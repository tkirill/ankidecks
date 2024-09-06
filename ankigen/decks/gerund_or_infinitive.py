from data.gerund_or_infinitive import read_gerund_or_infinitive_data, GerundOrInfinitiveItem, FollowedByEnum
from notes.output import write_notes_to_path
from notes.basic_example import BasicExampleNote
from concordance.skell import SkellConcordance


def get_query_for_item(item: GerundOrInfinitiveItem) -> str:
    match item.followed_by:
        case FollowedByEnum.gerund:
            return f'{item.verb} .*?ing'
        case FollowedByEnum.infinitive:
            return f'{item.verb} to [a-z]+'
        case FollowedByEnum.bare_infinitive:
            return f'{item.verb} '


def generate_gerunds_or_infinitive():
    data = read_gerund_or_infinitive_data('./data/gerund_or_infinitive.json')
    skell = SkellConcordance()
    notes = []
    for key, item in data.items():
        for followed_by in item.followed_by:
            query = get_query_for_item(item)
            examples = skell.get_examples(query)
            note = BasicExampleNote(key, followed_by, examples)
            notes.append(note)
    write_notes_to_path('gerund_or_infinitive.txt', notes)