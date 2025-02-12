import enum

class Util:

    @staticmethod
    def print_authors() -> None:
        print("//////////////////////////////////////")
        print("/// id:  308542141                ////")
        print("/// name: Elad Natan              ////")
        print("/// mail: elad.glx@email.com      ////")
        print("//////////////////////////////////////")
        print("/// id:   207930868               ////")
        print("/// name: Ofir Goldstein          ////")
        print("/// mail: goldsteinofir@gmail.com ////")
        print("//////////////////////////////////////\n")

    @staticmethod
    def Logger(msg: str, type: str = None):
        if type == 'e':
            print(f"[Error]: {msg}")
        elif type == 'i':
            print(f"[Info]: {msg}")
        else:
            print(msg)
