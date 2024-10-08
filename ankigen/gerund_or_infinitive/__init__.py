import json
import time

from ankigen.gerund_or_infinitive.models import GerundOrInfinitive, FollowedByEnum
from ankigen.notes.output import write_notes_to_path
from ankigen.notes.basic_example import BasicExampleNote
from ankigen.sketch.concordance import SketchConcordance


def read_gerund_or_infinitive_data(filename: str) -> GerundOrInfinitive:
    with open(filename) as f:
        raw = json.load(f)
    if '$schema' in raw:
        del raw['$schema']
    return GerundOrInfinitive.model_validate(raw)


def get_query_for_item(verb: str, followed_by: FollowedByEnum) -> str:
    match followed_by:
        case FollowedByEnum.gerund:
            return f'{verb} .*?ing'
        case FollowedByEnum.infinitive:
            return f'{verb} to [a-z]+'
        case FollowedByEnum.bare_infinitive:
            return f'{verb} '


def generate_gerunds_or_infinitive():
    data = read_gerund_or_infinitive_data('./ankigen/gerund_or_infinitive/gerund_or_infinitive.json')
    with SketchConcordance() as sketch:
        notes = []
        for key, item in data.root.items():
            for followed_by in item.followed_by:
                print(item.verb, followed_by, '...', end='')
                examples = sketch.get_examples_gerund_or_infinitive(item.verb, followed_by)
                examples.sort(key=len)
                short_examples = [x for x in examples if len(x) <= 150]
                del short_examples[20:]
                short_examples.extend('' for _ in range(20-len(short_examples)))
                tags = [f'gerund_or_infinitive::{followed_by}']
                note = BasicExampleNote(key, followed_by, short_examples, tags)
                notes.append(note)
                print('Success')
                time.sleep(5)
    write_notes_to_path('gerund_or_infinitive.txt', notes)