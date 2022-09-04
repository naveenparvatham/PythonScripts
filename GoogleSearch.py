# Performing google search using Python code
class gsearch_python:
    def __init__(self, name_search):
        self.name = name_search

    def gsearch(self):
        count = 0
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found.")
        for i in search(query=self.name, tld='co.in', lang='en', num=10,
                        stop=5, pause=2):
            count += 1
            print(count)
            print(i + '\n')


if __name__ == '__main__':
    gs = gsearch_python("Edureka")
    gs.gsearch()
