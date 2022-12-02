user_skills = set()
LOOKING_FOR = {
    'python': 1,
    'ruby': 2,
    'bash': 4,
    'git': 8,
    'html': 16,
    'tdd': 32,
    'css': 64,
    'javascript': 128
}

first_run = False
while True:
    while not first_run:
        print("We're looking for developers who know " +
              ", ".join(list(LOOKING_FOR.keys())).title() + ".")
        first_run = True
    skill_input = input(
        "What skills do you know? Type them one at a time. Type 'done' to calculate your score. ").lower()
    if skill_input == "done":
        break
    if skill_input in LOOKING_FOR.keys():
        user_skills.add(skill_input)

score = 0
for key in user_skills:
    score += LOOKING_FOR[key]

to_learn = False

if 'python' not in user_skills:
    to_learn = 'python'
if 'ruby' not in user_skills:
    to_learn = 'ruby'
if 'bash' not in user_skills:
    to_learn = 'bash'
if 'git' not in user_skills:
    to_learn = 'git'
if 'html' not in user_skills:
    to_learn = 'html'
if 'tdd' not in user_skills:
    to_learn = 'tdd'
if 'css' not in user_skills:
    to_learn = 'css'
if 'javascript' not in user_skills:
    to_learn = 'javascript'

if not to_learn:
    print(f"You have a perfect score of {score}! Congratulations.")
else:
    print(
        f"Your total score is {score}. To maximise your score, consider learning {to_learn}. It will increase your score by {LOOKING_FOR[to_learn]}!")
