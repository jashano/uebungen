class Roman:
    def __init__(self, roman):
        self.roman = roman
        self.decimal = self.roman_to_int(roman)

    def __str__(self):
        return self.roman

    def __add__(self, other):
        decimal = self.decimal + other.decimal
        roman = self.int_to_Roman(decimal)
        return Roman(roman)

    def roman_to_int(self, s):
        rom_val = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        int_val = 0
        i = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i-1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    def int_to_Roman(self, num):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syb = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_num = ""
        i=0
        while num > 0:
            for x in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
                i += 1
        return roman_num
    
a=Roman("MM")
print(a)