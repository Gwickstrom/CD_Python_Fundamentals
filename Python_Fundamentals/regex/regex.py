import re
# .   Matches any character except new line
# \w Matches any letter or digit
# +  The pattern before it can appear 1 or more times
# *  The pattern can appear any number of times, including none.

def get_matching_words(regex):
    words = ["aimlessness", "Assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", 
"facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress",
"millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", 
"schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

print(get_matching_words(r'v'))
print(get_matching_words(r'ss'))
print(get_matching_words(r'e$'))
print(get_matching_words(r'b.b'))
print(get_matching_words(r'b.+b'))
print(get_matching_words(r'b.*b'))
print(get_matching_words(r'a.*e.*i.*o.*u.*'))
print(get_matching_words(r'[regulaxpsion]'))
print(get_matching_words(r'(.)\1'))
print(get_matching_words(r'[A-Z]'))
