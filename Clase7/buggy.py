# Este programa coge un string y le pone raya al piso
# alrededor de cada caracter. Por ejemplo:
# Python --> _P_y_t_h_o_n_

def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        # Original: new_word = word[i] + "_"
        new_word = new_word + word[i] + "_" # arreglado
    return new_word

phrase = "hello" 
print(add_underscores(phrase)) # Espero _h_e_l_l_o_


# Pasos para debugging
# 1. Adivinar mas o menos por donde está el problema
# 2. Ponerle un breakpoint a ese lugar
# 3. Identificar el error y tratar de solucionar
# 4. Repetir 1 a 3 hasta arreglar el error
