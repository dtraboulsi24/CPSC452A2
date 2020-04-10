CPSC452A2

Daniel Traboulsi dtraboulsi@csu.fullerton.edu

William Clemons wclemons@csu.fullerton.edu

Programming Language: Python

Execute: 
    - AES:
        py A2.py AES "0123456789abcdef" ENC in.txt out.txt
        py A2.py AES "0123456789abcdef" DEC out.txt dec.txt
    - DES:
        py A2.py DES "01234567" ENC des_in.txt des_out.txt
        py A2.py DES "01234567" DES des_out.txt dec.txt
        
Info: Dependent on the pycryptodome package which can be installed by running the following command:
    - pip install pycryptodome