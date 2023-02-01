from instabot import Bot

bot = Bot()
# logged in on instagram using login() function
bot.login(username="esthetic__09", password="1026176152751")

# Follow and unfollow someone instagram using this
# bot.follow("geeks_for_geeks")
# bot.unfollow("geeks_for_geeks")

# Upload photos on instagram usnig
# bot.upload_photo(
#     "D:\PS\python-projects\Instagram Automation\download.jpeg", caption="I love Sunnah")

# Send meesage to the users
# if you want to send message to the multiple users, then put their names in the list
# bot.send_message("I love Sunnah", [
#                  "sahilkhankhan.khan", "shazad8401"])


# To get the info of the your follwers
# followers = bot.get_user_followers("esthetic__09")

# for follower in followers:
#     print(bot.get_user_info(followers))

# To get the info of the your follwers
following = bot.get_user_following("esthetic__09")

for Following in following:
    print(bot.get_user_info(Following), end="")
