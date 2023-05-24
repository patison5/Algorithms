l = [1,2,3,4,5]

d = {*l}



numbers = [1, 5, 2, 1, 7, 8]
result = 0
left = 0
windowSum = 0
k = 2

for current_index, number in enumerate(numbers):
	windowSum += number
	if current_index - left + 1 == k:
		result = max(result, windowSum)
		windowSum -= numbers[left]
		left += 1



def is_anagram(word: str, line: str) -> bool:
	if len(word) != len(line):
		return False
	matches = [0] * 26
	for char in word:
		matches[ord(char) - ord("a")] = 1

	for char in line:
		if matches[ord(char) - ord("a")] == 0:
			return False
	return True

def is_anagram(word: str, line: str) -> bool:
	if len(word) != len(line):
		return False
	frequensy_dict = {}
	for char in word:
		if char not in frequensy_dict:
			frequensy_dict[char] = 1
		else:
			frequensy_dict[char] += 1
	
	for char in line:
		if char not in frequensy_dict:
			return False
		frequensy_dict[char] -= 1
		if frequensy_dict[char] < 0:
			return False
	return True


def count_anagrams(word: str, line: str) -> int:
	result = 0
	left = 0
	window_line = ""
	for index in range(len(line)):
		window_line += line[index:index+1]
		print(window_line)
		if len(window_line) == len(word):
			if is_anagram(word, window_line):
				result += 1
			window_line = window_line[1:]
	return result

	

# line = "jtvlwhgjlnzaquhrgesgsmwyflrorjmojiyjdnnnhkmxalxyzwckttrrbdfellzwtmlidsiypqmifbbqnijfzdijluhkkfmausnfbmozcjioriwufexyyebzepmzhhmoxpevpumbnigmpubushpufzazqmjuzuurwgarjonhhdgoquxfgzxfceeiauzddilwhqaeuriftxgckepnlhanvwmieziznnpndhqmxptgcrzavkhctvvbuxuvmnwhlxoxuqtssawxqehbzgsgnqyiieuoupgvridkvgcnsbxrzzhtmjybrizuzshqsigahxeobqohrwxjhfxwwnhjyjtobqzdtehrwsblzzgvwzvrjdnlftcwxmankecnxczwwruzyqmwegttpwsljpbiyyfbxvfajytoetktldzryciwfdvlbyeiruzdlwzmwhwocegmhgmhbrbgeprjmkcqmyftzcibvgdvxlqmauzogjuhwscbsdzqjozjcemanjxaxzatikwxhxnfgrbytpsgonuczgvwdogfakaraejbvxzquycvtcuupaeawfetzjkqakarupmsogbojtdzobhhncarczjoqrayejlniadokrgoamrhtehxjfinlmeycauygvxuaxuitkuubjwvxqqtjenmeoypllwtuaibctwpjgrsgzwcvfxvjrvwvwjuhhvgydmwxzxekbwalutqcuumglkpyvpnejbtsdypwwnyjaykftsbcyfsbheclreuyzriuajasrusrzkfgblvqrlexmyefcrpuvzaryydrobqfhzikzpsnzwtzujuyeqatznqbxpkzhebnfyfvuudfvjtucclcqymthuvtpgzvnueqzswcgxgfqjiewmmgtmgkameoyzhzierotetpqvcvzxhnrxmendhnncvzhwkxhqvgsqidqzwhvxxkfyudrkjidvdrykzvpqqxbczafcaptypkjjaweuaxzviqomreqjvphritaupgdsgjlxlikhnujpqqqkscbswplkedswtofusmqtihcxtzjqcrxfxdssnosibzgrwngczaefakptrwhemmfknlaolmeblngqctsdoxentokgprtfvkidyyheotiqgbgepreaqbsidumcyqedocyuvkbykhuzbpjqrmyiqdqcouohalivsdxlfigsxqiovwrgaaygytuhymhnpzaxzdjfflanlyayzznwkzhdapegvbzrlzztkvrrrrkaoaalfbtdvwhbvhbetawpbbumkwdhpbrcyjrxlcljfuulsfpnpmclsloiogvqxuetuommepxdlawvsngyzzbausrbyrmjhrbpsjnqxbyietzgpaeqnqjhnuacaukssnkjfrfpbaklhaidpanouucpftyweazklrhbnctfezlhbmlmbiadqyawzfievnpzxngbnxtqlkiqpkahupkcbrwfsnwsovhkpnpukukdxbwptvwqrvkzzjshymbjknhvmcfknwnyyqerecdoeqsujkfoakqoikadiqitpwissgdswvdwfwmlraeegplbxmlpjyisyxjordxwteqyfxzpkfhfckmqslxoevlfysaszrpplvxyqqegspqisysravkdvfvihwejcmaearvdaomupwjiexfzakxooeczxyfbezqzbehguvvboyvkwptnmdlpuulecbirumewssdeoilgopovrjekjfxkwfmncpadxhortyxtvwfzhoqnfftkwoluwgmilqqtuxevpavrfgtsmbkpuayyqpspzmiidozyptzkcmbcqpcwmkdbowapcsfoqstnhghujthknsxlgjulpftcognnihtjxmexxbfkbrsjmrurygsgkvhmirorbjqrylckfsrdswvrxrjftdeihkakfwhexxsfgubuupzovclqfez"
# word = "xrwwzbgfjguccstiatvpwvwrvjvo"
# print(count_anagrams(word, line))

# for current_index, char in enumerate(line):


def average(salary: list[int]) -> float:
	salary = sorted(salary)
	index = 1
	sum = 0
	print(salary)
	while index < len(salary) - 1:
		sum += salary[index]
		print(salary[index])
		index += 1
	print(sum)
	return sum / (index - 1)

# print(average([4000,3000, 200]))



min = 5
fruits = [1,2,3,3,4,4,5]
# print(fruits[-1])

if fruits.pop() == min:
	min = fruits.pop()



print(min, fruits)
