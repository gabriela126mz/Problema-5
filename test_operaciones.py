import unittest 
from operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):

    #Caso de suma
    def test_sumar(self):
        self.assertEqual(sumar(1,1),2)
        self.assertEqual(sumar(-1,-1),-2) 
        self.assertEqual(sumar(0,0),0) 
        self.assertEqual(sumar(-1,1),0) 

    def test_sumar_string(self):
        with self.assertRaises(TypeError):
            sumar('Hello',1)
            sumar('Hello','Bye')
            sumar(1,'Bye')

    #Caso de resta
    def test_resta(self):
        self.assertEqual(restar(1,1),0) 
        self.assertEqual(restar(-1,-1),0) 
        self.assertEqual(restar(0,0),0) 
        self.assertEqual(restar(-1,1),-2)

    def test_restar_string(self):
        with self.assertRaises(TypeError): 
            restar('Hello',1)
            restar('Hello','Bye')
            restar(1,'Bye')

    #Caso de multiplicación
    def test_multiplicar(self):
        self.assertEqual(multiplicar(1,1),1) 
        self.assertEqual(multiplicar(-1,-1),1) 
        self.assertEqual(multiplicar(0,0),0) 
        self.assertEqual(multiplicar(-1,1),-1)
   
    def test_multiplicar_string(self):
        with self.assertRaises(TypeError): 
            multiplicar('Hello',1)
            multiplicar('Hello','Bye')
            multiplicar(1,'Bye')
      
    #Caso de división
    def test_dividir(self):
        self.assertEqual(dividir(1,1),1) 
        self.assertEqual(dividir(-1,-1),1) 
        self.assertEqual(dividir(-1,1),-1)
       
    def test_dividir_string(self):
        with self.assertRaises(TypeError): 
            dividir('Hello',1)
            dividir('Hello','Bye')
            dividir(1,'Bye')
         
    def test_dividir_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
    
if __name__ == '__main__':
    unittest.main()


