class TemplateException(Exception):
    pass


class RichStr:
    def get_context(self):
        return self.__dict__

    def get_template(self):
        try:
            return self.TEMPLATE
        except AttributeError:
            raise TemplateException("RichStr: template not defined.")

    def __str__(self):
        return self.get_template().format(**self.get_context())


class RichStrList:
    SEPARATOR = '\n'
    TEMPLATE = None

    def __init__(self, l):
        class InnerRichText(RichStr):
            TEMPLATE = self.TEMPLATE

            def __init__(self, dic):
                self.dic = dic

            def get_context(self):
                return self.dic

        self.l = map(InnerRichText, l)

    def __str__(self):
        return self.SEPARATOR.join(map(str, self.l))
