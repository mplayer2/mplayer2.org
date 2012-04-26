import os, re

class Post(object):
    def __init__(self, path):
        self.path = path

    @property
    def title(self):
        self.__parse_data()
        return self.__title

    @property
    def author(self):
        self.__parse_data()
        return self.__author

    @property
    def date(self):
       return "/".join(self.__date_array())

    @property
    def abstract(self):
        self.__parse_data()
        return self.__abstract

    @property
    def body(self):
        self.__parse_data()
        return self.__body

    def __date_array(self):
        day_p   = os.path.dirname(self.path)
        month_p = os.path.dirname(day_p)
        year_p  = os.path.dirname(month_p)
        return [os.path.basename(x) for x in [day_p, month_p, year_p]]

    def __parse_data(self):
        _in_abstract, _in_body = False, False
        _abstract_ary, _body_ary = [], []
        for line in self.__get_file_data():
            g = re.search("^\.\. title: (.*)$", line)
            if g:
                self.__title = g.group(1)
                continue

            g = re.search("^\.\. author: (.*)$", line)
            if g:
                self.__author = g.group(1)
                continue

            g = re.search("^\.\. abstract$", line)
            if g:
                _in_abstract = True
                continue

            g = re.search("^\.\. body$", line)
            if g:
                _in_abstract = False
                _in_body = True
                continue

            if _in_abstract:
                _abstract_ary.append(line)
                continue

            if _in_body:
                _body_ary.append(line)
                continue

        self.__abstract = "".join(_abstract_ary).strip()
        self.__body = "".join(_body_ary).strip()

    def __get_file_data(self):
        f = open(self.path, "r")
        result = f.readlines()
        f.close()
        return result

