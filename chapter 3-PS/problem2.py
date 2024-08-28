# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
import datetime

name = input('Enter your name : ');
curr_date = datetime.date.today();
print()
letter = 'Dear '+name +'\nyou are selected!\n'+str(curr_date);
print(letter);