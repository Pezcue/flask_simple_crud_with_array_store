usuarios = ["ade", "rdx", "foo", "mek"]

usuario = "foo"
nuevo_usuario = "toto"

for idx in range(len(usuarios)):
   if usuarios[idx] == usuario:
      usuarios[idx] = nuevo_usuario

print(usuarios)
