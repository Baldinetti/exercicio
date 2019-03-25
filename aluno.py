#coding: utf-8
class Aluno:
    nome = ""
    ra = 0
<<<<<<< HEAD
    
    def __init__(self, nome="", ra=0):
        self.nome = nome
        self.ra = ra
=======
    curso = ""
    
    def __init__(self, nome="", ra=0, curso= ""):
        self.nome = nome
        self.ra = ra
        self.curso = curso
>>>>>>> dev2
    
    def __del__(self):
        print("Finalizando")
    
    def mostraAluno(self):
        print("Nome: %s" % self.nome)
        print("R.A.: %d" % self.ra)
<<<<<<< HEAD
        
=======
        print("Curso: %s" % self.curso)
>>>>>>> dev2
        
        
