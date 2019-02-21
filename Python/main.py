from program import Generic

class Main:

  @staticmethod
  def run ():

    # Dataset   
    base_a  = 'C:/Users/kleytonramos/Documents/Merge de Nome - Genérico/bases/base_a.xlsx'
    sheet_a = '2017'

    base_b  = 'C:/Users/kleytonramos/Documents/Merge de Nome - Genérico/bases/base_b.xlsx'
    sheet_b = '2018'
    
    # # Dataset output
    output  = 'C:/Users/kleytonramos/Documents/Merge de Nome - Genérico/bases/saida.xlsx'

    # # set variable name 
    key_a   = 'cd_escola'
    nm_a    = 'nm_aluno'
    extra_a = 'cd_aluno'
    
    key_b   = 'cod_design'
    nm_b    = 'nm_aluno'
    extra_b = 'serie'

    r = Generic (base_a, base_b, sheet_a, sheet_b, nm_a, nm_b, key_a, key_b, extra_a, extra_b)
    r.export(output)
    r.append
      
Main.run()   


  


