from ankigen.data.gerund_or_infinitive import read_gerund_or_infinitive_data, GerundOrInfinitiveItem, FollowedByEnum
from ankigen.notes.output import write_notes_to_path
from ankigen.notes.basic_example import BasicExampleNote
from ankigen.concordance.skell import SkellConcordance


def get_query_for_item(verb: str, followed_by: FollowedByEnum) -> str:
    match followed_by:
        case FollowedByEnum.gerund:
            return f'{verb} .*?ing'
        case FollowedByEnum.infinitive:
            return f'{verb} to [a-z]+'
        case FollowedByEnum.bare_infinitive:
            return f'{verb} '


def generate_gerunds_or_infinitive():
    data = read_gerund_or_infinitive_data('./ankigen/data/gerund_or_infinitive.json')
    skell = SkellConcordance()
    notes = []
    for key, item in data.items():
        for followed_by in item.followed_by:
            query = get_query_for_item(item.verb, followed_by)
            examples = skell.get_examples(query)
            tags = [f'gerund_or_infinitive::{followed_by}']
            note = BasicExampleNote(key, followed_by, examples, tags)
            notes.append(note)
    write_notes_to_path('gerund_or_infinitive.txt', notes)