from bulletin.section import Section


class Test_Addon(Section):
    def __init__(self, config={}):
        super().__init__(self._test, "test.html", config)


    @staticmethod
    def _test(config):
        return {"THIS IS A TEST"}

