import xml.etree.ElementTree as etree


class XmlWorker:
    params = {}

    def __init__(self, file):
        self.config = etree.parse(file)
        self.params_extractor()

    def params_extractor(self):
        for child in self.config.getroot():
            print(str(child.tag))
            self.params[str(child.tag)] = self.config.find(str(child.tag)).text

    def get_values(self):
        return self.params
