from ankigen.skell.models import SkellConcordanceResponse


class SkellClient:
    
    def search(self, query: str) -> SkellConcordanceResponse:
        return f'Response for {query}'