import vim

registers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'q', 'z', '-', '.', ':', '%', '/', '"', '=']
register_contents = '\t'.join([vim.eval('@' + r) for r in registers])
mode = vim.eval("mode()")
file_contents = '\n'.join(vim.current.buffer)
cursor = ' '.join([str(c) for c in vim.current.window.cursor])

with open("state/registers.txt", "w+") as f:
    f.write(register_contents)
with open("state/mode.txt", "w+") as f:
    f.write(mode)
with open("state/contents.txt", "w+") as f:
    f.write(file_contents)
with open("state/cursor.txt", "w+") as f:
    f.write(cursor)
