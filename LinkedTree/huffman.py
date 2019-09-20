from organization import Organization

class Huffman:
    listOrganized = list(str(input("Digite uma série de caracteres: ")))
    listOrganized = Organization.setlistwords(listOrganized)    

if __name__ == "__main__":
    Huffman()