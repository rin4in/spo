alien = '''
public class Test {

   public static void main(String[] args) { \\ short comment
                                          
      String a; /* long comment */
      String b;

      a = "Hello";
      b = "world";

      System.out.println(a + b);
   }
}
'''

lst = []

single_char = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',',';'] 
double_char = ['\\', '/*', '*/'] 
words = ['public', 'class', 'void', 'main', 'String', 'int']
KEYWORDS = single_char + double_char + words

space = ' '

lex = ''

for i,char in enumerate(alien):
	if char == '*':
		if alien[i-1] == '/':
			lex += '/*'
		elif alien[i+1] == '/':
			lex += '*/'
		else:
			lex += '*'
	elif char == '/':
		if alien[i+1] != '*' and alien[i-1] != '*':
			lex += '/'
		else:
			continue
	else:
		if char != space:
			lex += char
		if (i+1 < len(alien)):
			if alien[i+1] == space or alien[i+1] in KEYWORDS or lex in KEYWORDS:
				if lex != '':
					lst.append(lex)
					lex = ''
print(lst)

print('#'*100)

final_lst = []


for c in lst:
	if c in single_char:
		new_list = ['single_char']
		new_list+=c
		final_lst.append(new_list)
	elif c in double_char:
		new_list = ['double_char']
		new_list.append(c)
		final_lst.append(new_list)
	elif c in words:
		new_list = ['words']
		new_list.append(c)
		final_lst.append(new_list)
	else:
		continue	
print(final_lst)
