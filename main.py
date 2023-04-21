import argparse
import random
import sys
import time
from itertools import cycle, product


def pprint(s, end="\n", wpm=100):
    """print like ChatGPT"""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / wpm)
    print(end, end="")


positive_messages = [
    "すごいね！🌟",
    "せいかいだよ！👍",
    "やったね、かんたんすぎるね！😁",
    "えらいね！👏",
    "ばんざい！🎉",
    "すばらしい！😊",
    "やったー！🎊",
    "ほんとうにすごいね！🚀",
    "すごい、もうプロだね！🏆",
    "とってもえらいね！💯",
    "さいこうだね！🥇",
    "たのしいね！🎈",
    "これはあっというまだね！😄",
    "おおすごい！🌈",
    "これでぼくたちのチームがつよくなるね！💪",
    "ほんとうにかしこいね！🧠",
    "かんぺきだね！✨",
    "おめでとう！🌠",
    "いいかんじだね！🌟",
    "ほんとうにじょうずだね！👌",
    "わお、さいこうだね！🎆",
    "えいえんのゆうしゃだね！🦸",
    "おお、もうかんぺきだね！🎯",
    "これはもうプロだね！🔥",
    "すごい、もうかんぺきだね！🌟",
    "もうすごいじょうずだね！👏",
    "これでおおもうけだね！💰",
    "うれしいね！😃",
    "すごい、もうかんぺきだね！👌",
    "これでぼくたちのチームがつよくなるね！🎉",
]

negative_messages = [
    "あれれ？😅",
    "いいよ、もういちどためしてみよう！👍",
    "むずかしいけど、がんばってね！💪",
    "だいじょうぶ、ちょっとずつできるようになるよ！🌱",
    "もういちどためしてみよう！😄",
    "おお、ちょっとちがうね。もういちど！🎈",
    "ふんばって、もうすこし！🔥",
    "ちょっとちがうけど、だいじょうぶ！😊",
    "ぜったいできるよ！💪",
    "だいじょうぶ、もうちょっとだけ！🚀",
    "もうすこしだけ、がんばってね！🌟",
    "ちょっとちがうけど、ふんばってね！💯",
    "もうちょっとだけ、あきらめめないで！🌈",
    "だいじょうぶ、おおきなゆめをかなえよう！🌠",
    "ちょっとちがうけど、かんぺきになるまでがんばろう！🎯",
    "だいじょうぶ、じょうずになるまでたいせつだね！💖",
    "もうちょっとだけ、しんぼうしてね！🌱",
    "だいじょうぶ、きっとできるよ！👍",
    "ちょっとちがうけど、もうすこし！✨",
    "もうすこしだけ、がんばってね！💪",
    "だいじょうぶ、いっしょにがんばろう！👫",
    "もうちょっとだけ、あきらめないでね！🌟",
    "ちょっとちがうけど、だいじょうぶ！😃",
    "だいじょうぶ、きっとじょうずになるよ！👌",
    "ちょっとちがうけど、もうすこし！🎉",
    "だいじょうぶ、いっしょにがんばろうね！💖",
    "もうちょっとだけ、しんぼうしてね！🌱",
    "だいじょうぶ、いっしょにがんばろう！👍",
    "ちょっとちがうけど、もうすこし！✨",
    "もうちょっとだけ、がんばってね！💪",
    "だいじょうぶ、いっしょにがんばろう！👫",
    "もうちょっとだけ、あきらめないでね！🌟",
]

random.shuffle(positive_messages)
positive_messages = cycle(positive_messages)
random.shuffle(negative_messages)
negative_messages = cycle(negative_messages)

NUM = {
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣",
    9: "9️⃣",
    10: "🔟",
}

# Set up argument parsing
parser = argparse.ArgumentParser(description="Multiplication table quiz")
parser.add_argument("-n", default=10, type=int)
parser.add_argument(
    "factors", type=int, nargs="+", help="Values to use for the first factor"
)
args = parser.parse_args()

N = args.n

questions = list(product(args.factors, range(2, 10)))
random.shuffle(questions)
questions = questions[:N]

score = 0
space = " " * 10
for i, (a, b) in enumerate(questions):
    print()
    print("=============")
    pprint(f" しつもん {NUM[i+1]}")
    print("=============")
    print()

    while True:
        print()
        pprint(f"     {a} x {b} = ", end="")
        ui = input()
        print()
        try:
            ui = int(ui)
        except ValueError:
            pprint("??? try again!")
            print()
        if ui == a * b:
            if i + 1 < N:
                m = next(positive_messages)
                print(space, end="")
                pprint(m)
            score += 1
            break

        m = next(negative_messages)
        print(space, end="")
        pprint(m)

print()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
pprint(f"You got {score} out of {N} questions correct. 💯")
pprint("Well done! 😊")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
# print("✨ 🚀 🌟 ✨ 🚀 🌟 ✨ 🚀 🌟 ✨ 🚀 🌟 ")
# print("🎉 🎉 🎉   😊 😊 😊   🎊 🎊 🎊")
