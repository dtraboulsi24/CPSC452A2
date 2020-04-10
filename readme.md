CPSC452A2

Daniel Traboulsi dtraboulsi@csu.fullerton.edu

William Clemons wclemons@csu.fullerton.edu

Programming Language: Python

Execute: 
    - AES:
        py A2.py AES "0123456789abcdef" ENC aes_in.txt aes_out.txt
        py A2.py AES "0123456789abcdef" DEC aes_out.txt aes_dec.txt
    - DES:
        py A2.py DES "01234567" ENC des_in.txt des_out.txt
        py A2.py DES "01234567" DEC des_out.txt des_dec.txt

Info: Dependent on the pycryptodome package which can be installed by running the following command:
    - pip install pycryptodome
    - Test files have been included, the same commands that are shown above should work and allow execution directly after unzipping
    - Print statements are left in on purpose to show the project as it works through the steps.
    - No Extra Credit was attempted.