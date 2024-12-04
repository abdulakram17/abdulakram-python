#String concatenation(how to put strings together)
#We want to create a string that says 'Follow my Linkedin Profile'
linkedin='zainakram'
insta='zainakram'
ytb='Abdulakram'
print('Follow to my linkedIn',linkedin)
print('Follow to my instagram {}'.format(insta))
print(f'Subscibe to youtube channel {ytb}')
# I Go with f string because its the cleanest way to Express string concatenation.
print('Welcome to the madlibs game')
print('Fill the blanks to introce yourself')
name=input('Enter your name::')
place=input('Enter the place:')
branch=input('Enter the branch of engineering::')
CGPA=float(input('Enter the cgpa ::'))
clgname=input('Enter the clgname::')
game=input('Enter the games u liked to play:')
book=input('Enter the books u like:')
codinglang=input('Enter the programming language')
skills=input('Enter the skills you know ::')
print(f'Myself {name} I am from {place} I recently completed my bachelor of engineering in {branch} with a {CGPA} from {clgname}.My Hobbies is to play {game}. I Love {codinglang} .My favourite book is {book}. My Skills are {skills}. ')
