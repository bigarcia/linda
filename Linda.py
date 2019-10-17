class LindaTuplaSpace():

    __instance = None

    @staticmethod
    def get_instance():
        if not LindaTuplaSpace.__instance:
            LindaTuplaSpace.__instance = LindaTuplaSpace()
        return LindaTuplaSpace.__instance

    def __init__(self):
        self.tuples = []

    def _out(self,tuple):
        self.tuples.append(tuple)
        return (tuple)

    def _in(self, tuple):
        for tuple_base in self.tuples:
            if(tuple == tuple_base):
                self.tuples.remove(tuple_base)
                return tuple
        return False

    def _rd(self, tuple):
        response = []
        for tuple_base in self.tuples:
            aux = tuple
            if( 
                (tuple[0] == tuple_base[0] or tuple[0] == str)
                and (tuple[1] == tuple_base[1] or tuple[1] == str)
                and (tuple[2] == tuple_base[2] or tuple[2] == str)
            ):response.append(tuple_base)

        if(len(response) != 0):
            return response
        return []
