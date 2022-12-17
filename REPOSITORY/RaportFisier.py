from REPOSITORY.repo import *


class RaportFisier:
    def __init__(self, fileName):
        self.fileName = fileName

    def store(self, d, maxi):
        f = open(self.fileName, "w")
        for k, v in d.items():
            if v == maxi:
                f.write(f'Persoana cu id-ul {k} are cele mai multe evenimente: {maxi}\n')
        f.close()
