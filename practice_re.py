import re

search_text = "Several rapidly developing RNA interference (RNAi) methodologies hold the promise to selectively inhibit gene expression in mammals. RNAi is an innate cellular process activated when a double-stranded RNA (dsRNA) molecule of greater than 19 duplex nucleotides enters the cell, causing the degradation of not only the invading dsRNA molecule, but also single-stranded (ssRNAs) RNAs of identical sequences, including endogenous mRNAs."


matches = re.finditer(r"\S\w*RNA\S*\w*\S", search_text)

for m in matches:
    nucleic_acid = m.group()
    pos = m.end() - 1
    print(nucleic_acid, "ends at position", str(pos))

