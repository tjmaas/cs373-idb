from haystack.forms import SearchForm


class GlobalSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()