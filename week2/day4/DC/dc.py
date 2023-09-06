    #  i take no credit for this.  had to look up almost every lit bit of this.  learned a lot though
    
    # 7ii
    # Tsx
    # h%?
    # i #
    # sM 
    # $a 
    # #t%
    # ^r!
    
matrix = [
    ["7", "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", "", "#"],
    ["s", "M", ""],
    ["$", "a", ""],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

transposed_matrix = list(map(list, zip(*matrix)))

code = ""
    
for column in transposed_matrix :
    for cell in column:
        if cell.isalpha():
            code += cell
       
               
print(code)
         
    
    