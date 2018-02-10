import vim

REGISTERS = [chr(x) for x in range(34,122)]
register_contents = '\t'.join([vim.eval('@' + r) for r in REGISTERS])
mode = vim.eval("mode()")
file_contents = '\n'.join(vim.current.buffer)
cursor = ' '.join([str(c) for c in vim.current.window.cursor])

with open("environment/state/registers.txt", "w+") as f:
    f.write(register_contents)
with open("environment/state/mode.txt", "w+") as f:
    f.write(mode)
with open("environment/state/contents.txt", "w+") as f:
    f.write(file_contents)
with open("environment/state/cursor.txt", "w+") as f:
    f.write(cursor)
