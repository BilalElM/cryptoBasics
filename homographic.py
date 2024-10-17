import tenseal as ts
# als tenseal niet meteen werkt doe pip install NumPy maakt gebruik van deze libary
context = ts.context(ts.SCHEME_TYPE.BFV,
                     poly_modulus_degree=4096, plain_modulus=1032193)


context.generate_galois_keys()
context.generate_relin_keys()


num1 = ts.bfv_vector(context, [75])
num2 = ts.bfv_vector(context, [326])


enc_result = num1 + num2


dec_result = enc_result.decrypt()
# print("Getal 1 na encryptie: ", num1.serialize())
# print("Getal 2 na encryptie: ", num2.serialize())

print("Resultaat: ", dec_result[0])
