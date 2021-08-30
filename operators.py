# Program do liczenia VATu za usługę transportową


freight1 = 3400
freight2 = 1900
VAT = 0.23
VATmodifier = 1 + VAT

freight1VAT = freight1 * VATmodifier
freight2VAT = freight2 * VATmodifier

print("fracht pierwszy", freight1)
print("fracht pierwszy z podakiem", freight1VAT)

print("czy pierwszy większy?", freight1VAT < freight2VAT)
