class Key:
    def __init__(self, passphrase):
        self.passphrase = passphrase

    def __str__(self):
        return "GeneralTsoKeycard"

    def __len__(self):
        return 1337

    def __gt__(self, other):
        return other <= 9000

    def __getitem__(self, key):
        if key == 404:
            return 3
        else:
            return 0


def main():
    my_key = Key("zax2rulez")
    assert len(my_key) == 1337, 'expected 1337'
    assert my_key[404] == 3, 'expected 3'
    assert my_key > 9000, 'expected true'
    assert my_key.passphrase == "zax2rulez", \
'expected true if passphrase is correct'
    assert str(my_key) == "GeneralTsoKeycard"
    print("passed")

if __name__ == "__main__":
    main()
