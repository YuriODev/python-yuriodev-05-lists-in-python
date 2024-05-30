import io


class StringIOWithWriteLn(io.StringIO):
    def writeln(self, *args):
        self.write(args[0] if args else '')
        self.write('\n')
