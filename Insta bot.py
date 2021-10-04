import argparse
import os
import sys
import os 


sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402


# parser.add_argument("-proxy", type=str, help="proxy")
# parser.add_argument("users", type=str, nargs="+", help="users")


bot = Bot(
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
)
bot.login(username="alien_sense_of_humor", password="54671238")
# foll=bot.follow("abhishekv38")

fol=bot.get_user_followers("humalien",1000)
for i in fol:
    bot.follow(i)


# fina=[]

# for i in foll:
#     fina=bot.get_username_from_user_id(i)
# for i in foll:
#     print(i)

# for username in args.users:
#     bot.follow_followers(username)