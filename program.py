from tkinter import *
from tkinter import messagebox
from pyrogram import Client
from pyrogram.api import functions
import asyncio

"""Author: Ido Nidbach
begin: 22.5.2019
finish: 10.6.2019

This program basically allows you to number of things. it allows you to send messages, create group chats and adding
users to it, send an image or a sticker and send your message in a time of your choice up to 24 hours.

To start using the program you'll need three main things:

1. choosing a name for your session

2. API ID

3. API HASH

The first one is easy, the other two requires you to enter the next url: "my.telegram.org"
in this site you enter the phone number of your new user in telegram. you then go in "development tools" and fill
the requested fields. you have now created your new app! congratulations!

After creating your new app you receive both API ID and API HASH.
you are now ready for using the program's client method.
you enter the arguments for the client method in order to create a user. in this program, the client method is 
called: user. Once you enter the arguments for the user you can start using the program features.
the arguments are:

1. name of the session you connect with your user(you choose the name of the session).
 
2. your API ID number which you get in "my.telegram.org".

3. your API HASH code as a string which you get in "my.telegram.org". 

After entering those arguments you'll need to enter your proxy's hostname and port number.
you can now use the program's features! 

The first feature is creating a new group chat with up to 10 users.
you enter a name for your new group and write what it's all about.
next you fill in the fields that sits next the "invite users buttons". in each field you enter one username. minimum 
2 users. lets say you've entered 2 usernames, in order to invite them you'll need to enter the group's link(make sure 
to know if your group is private or not and then you'll know it's link. so you enter the link, then you press on 
"invite 2 users" button. the users have been added to your group chat.

The next feature is message sending in a couple of aspects:

1. sending a regular message

2. sending an image

3. sending a sticker

4. sending a timed message

You enter the username of the person who receives the message.
then you enter your message or image link or sticker code
if your message is a text message you press "send message", if it's an image you press "send image" and if
it's a sticker you press "send sticker"

In order to send a timed message you enter the receiver's username and your message(or image link or sticker code) 
and press on time button you choose, for instance if you want to send the message one minute from now you press 
"send in 1 minute".

Enjoy your Telepy experience and do not spam!
"""

# open the program window Telepy

app = Tk()
app.title("Telepy")
app.configure(background="light blue")
app.geometry("1100x750")


# saves the session's name, API ID and API HASH in the text file "user info.txt"
# and then deletes the input for inserting new input


def save_info():
    session_info = entry_session.get()
    api_id_info = entry_api_id.get()
    api_id_info = str(api_id_info)
    api_hash_info = entry_api_hash.get()

    file = open("user info.txt", "w")
    file.write(session_info)
    file.write("\n")
    file.write(api_id_info)
    file.write("\n")
    file.write(api_hash_info)
    file.close()
    print(messagebox.showinfo(title="message", message="user info saved in a text file: 'user info.txt'"))

    entry_session.delete(0, END)
    entry_api_id.delete(0, END)
    entry_api_hash.delete(0, END)


# the programs's labels(headers) in the user and group sections


Label(app, text="Welcome to Telepy!!", bg="green", fg="blue", font="Times 20").grid(row=0, column=0,
                                                                                    sticky=W)
Label(app, text="Send messages to Telegram via Telepy!",
      bg="grey", fg="black", font="Times 13").grid(row=1, column=0, sticky=W)
Label(app, text="For creating a user", bg="light green", fg="black", font="Arial 15").grid(row=2, column=0, sticky=W)
Label(app, text="Enter your session's name:", bg="blue", fg="black", font="Arial 10").grid(row=3, column=0,
                                                                                           sticky=W)
Label(app, text="Enter your Api ID:", bg="blue", fg="black", font="Arial 10").grid(row=4, column=0, sticky=W)
Label(app, text="Enter your Api Hash:", bg="blue", fg="black", font="Arial 10").grid(row=5, column=0, sticky=W)
Label(app, text="Enter your proxy hostname:", bg="blue", fg="black", font="Arial 10") \
    .grid(row=7, column=0, sticky=W)
Label(app, text="Enter your proxy port:", bg="blue", fg="black", font="Arial 10").grid(row=8, column=0, sticky=W)
Label(app, text="-----------------------------------------", bg="light blue", fg="black") \
    .grid(row=9, column=0, sticky=W)
Label(app, text="For creating a group:", bg="light green", fg="black", font="Arial 15") \
    .grid(row=10, column=0, sticky=W)
Label(app, text="Enter a name for your group:", bg="blue", fg="black", font="Arial 10").grid(row=11, column=0,
                                                                                             sticky=W)
Label(app, text="What is your group all about:", bg="blue", fg="black", font="Arial 10") \
    .grid(row=12, column=0, sticky=W)
Label(app, text="Enter the group's link:", bg="blue", fg="black", font="Arial 10") \
    .grid(row=14, column=0, sticky=W)
Label(app, text="usernames:", bg="light green", fg="black", font="Arial 10").grid(row=16, column=1, sticky=W)

# setting the API ID and port as integers

api_id = IntVar()
port = IntVar()

# the program's entry inputs(user and group section)

entry_session = Entry(app, width=30, bg="grey", fg="blue", font="Arial 10")
entry_session.grid(row=3, column=1, sticky=W)

entry_api_id = Entry(app, textvariable=api_id, width=30, bg="grey", fg="blue", font="Arial 10")
entry_api_id.grid(row=4, column=1, sticky=W)

entry_api_hash = Entry(app, width=35, bg="grey", fg="blue", font="Arial 10")
entry_api_hash.grid(row=5, column=1, sticky=W)

entry_hostname = Entry(app, width=30, bg="grey", fg="blue", font="Arial 10")
entry_hostname.grid(row=7, column=1, sticky=W)

entry_port = Entry(app, textvariable=port, width=30, bg="grey", fg="blue", font="Arial 10")
entry_port.grid(row=8, column=1, sticky=W)

entry_group_name = Entry(app, width=30, bg="grey", fg="blue", font="Arial 10")
entry_group_name.grid(row=11, column=1, sticky=W)

entry_group_description = Entry(app, width=30, bg="grey", fg="blue", font="Arial 10")
entry_group_description.grid(row=12, column=1, sticky=W)

entry_group_link = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
entry_group_link.grid(row=14, column=1, sticky=W)

# username entry inputs(group section)

username1 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username1.grid(row=17, column=1, sticky=W)

username2 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username2.grid(row=18, column=1, sticky=W)

username3 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username3.grid(row=19, column=1, sticky=W)

username4 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username4.grid(row=20, column=1, sticky=W)

username5 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username5.grid(row=21, column=1, sticky=W)

username6 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username6.grid(row=22, column=1, sticky=W)

username7 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username7.grid(row=23, column=1, sticky=W)

username8 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username8.grid(row=24, column=1, sticky=W)

username9 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username9.grid(row=25, column=1, sticky=W)

username10 = Entry(app, width=20, bg="grey", fg="blue", font="Arial 10")
username10.grid(row=26, column=1, sticky=W)

# message section
# labels(headers) and entry inputs message section

Label(app, text="Enter the receiver's username here:", bg="blue", fg="black", font="Arial 10") \
    .grid(row=0, column=2, sticky=W)
Label(app, text="Enter your message here:", bg="blue", fg="black", font="Arial 10").grid(row=1, column=2, sticky=W)
Label(app, text="Enter your image link here:", bg="blue", fg="black", font="Arial 10") \
    .grid(row=2, column=2, sticky=W)
Label(app, text="Enter you sticker code here:", bg="blue", fg="black", font="Arial 10") \
    .grid(row=3, column=2, sticky=W)

receiver_user_entry = Entry(app, width=30, bg="white", fg="black", font="Arial 10")
receiver_user_entry.grid(row=0, column=3, sticky=W)

message_entry = Entry(app, width=50, bg="white", fg="black", font="Arial 10")
message_entry.grid(row=1, column=3, sticky=W)

image_entry = Entry(app, width=30, bg="white", fg="black", font="Arial 10")
image_entry.grid(row=2, column=3, sticky=W)

sticker_entry = Entry(app, width=50, bg="white", fg="black", font="Arial 10")
sticker_entry.grid(row=3, column=3, sticky=W)


# send a regular message function


def send_a_message_no_proxy():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get())
    user.start()
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_a_message():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


# send an image function


def send_an_image():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send_message(receiver_user_entry.get(), image_entry.get())
    return


# send a sticker function


def send_a_sticker():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send_message(receiver_user_entry.get(), sticker_entry.get())
    return


# create a group function


def create_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.CreateChannel(title=entry_group_name.get(), about=entry_group_description.get(),
                                               megagroup=True))
    return


# invite 2 users to a group


def invite_2_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get())]))
    return


# invite 3 users to a group


def invite_3_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get())]))
    return


# invite 4 users to a group


def invite_4_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get())]))
    return


# invite 5 users to a group


def invite_5_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get()),
                                                        user.resolve_peer(username5.get())]))
    return


# invite 6 users to a group


def invite_6_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get()),
                                                        user.resolve_peer(username5.get()),
                                                        user.resolve_peer(username6.get())]))
    return


# invite 7 users to a group


def invite_7_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get()),
                                                        user.resolve_peer(username5.get()),
                                                        user.resolve_peer(username6.get()),
                                                        user.resolve_peer(username7.get())]))
    return


# invite 8 users to a group


def invite_8_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get()),
                                                        user.resolve_peer(username5.get()),
                                                        user.resolve_peer(username6.get()),
                                                        user.resolve_peer(username7.get()),
                                                        user.resolve_peer(username8.get())]))
    return


# invite 9 users to a group


def invite_9_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get()),
                                                        user.resolve_peer(username5.get()),
                                                        user.resolve_peer(username6.get()),
                                                        user.resolve_peer(username7.get()),
                                                        user.resolve_peer(username8.get()),
                                                        user.resolve_peer(username9.get())]))
    return


# invite 10 users to a group


def invite_10_users_to_group():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    user.send(functions.channels.InviteToChannel(channel=user.resolve_peer(entry_group_link.get()),
                                                 users=[user.resolve_peer(username1.get()),
                                                        user.resolve_peer(username2.get()),
                                                        user.resolve_peer(username3.get()),
                                                        user.resolve_peer(username4.get()),
                                                        user.resolve_peer(username5.get()),
                                                        user.resolve_peer(username6.get()),
                                                        user.resolve_peer(username7.get()),
                                                        user.resolve_peer(username8.get()),
                                                        user.resolve_peer(username9.get()),
                                                        user.resolve_peer(username10.get())]))
    return


# Timing functions
# each function with it's own time countdown by asyncio.sleep method which accepts the argument in seconds


async def in_one_minute():
    one_minute = await asyncio.sleep(60)
    return one_minute


async def in_ten_minutes():
    ten_minutes = await asyncio.sleep(600)
    return ten_minutes


async def in_twenty_minutes():
    twenty_minutes = await asyncio.sleep(1200)
    return twenty_minutes


async def in_thirty_minutes():
    thirty_minutes = await asyncio.sleep(1800)
    return thirty_minutes


async def in_fourty_minutes():
    forty_minutes = await asyncio.sleep(2400)
    return forty_minutes


async def in_thifty_minutes():
    fifty_minutes = await asyncio.sleep(3000)
    return fifty_minutes


async def in_one_hour():
    one_hour = await asyncio.sleep(3600)
    return one_hour


async def in_two_hours():
    two_hours = await asyncio.sleep(7200)
    return two_hours


async def in_three_hours():
    three_hours = await asyncio.sleep(10800)
    return three_hours


async def in_four_hours():
    four_hours = await asyncio.sleep(14400)
    return four_hours


async def in_five_hours():
    five_hours = await asyncio.sleep(18000)
    return five_hours


async def in_six_hours():
    six_hours = await asyncio.sleep(21600)
    return six_hours


async def in_seven_hours():
    seven_hours = await asyncio.sleep(25200)
    return seven_hours


async def in_eight_hours():
    eight_hours = await asyncio.sleep(28800)
    return eight_hours


async def in_nine_hours():
    nine_hours = await asyncio.sleep(32400)
    return nine_hours


async def in_ten_hours():
    ten_hours = await asyncio.sleep(36000)
    return ten_hours


async def in_eleven_hours():
    eleven_hours = await asyncio.sleep(39600)
    return eleven_hours


async def in_twelve_hours():
    twelve_hours = await asyncio.sleep(43200)
    return twelve_hours


async def in_thirteen_hours():
    thirteen_hours = await asyncio.sleep(46800)
    return thirteen_hours


async def in_fourteen_hours():
    fourteen_hours = await asyncio.sleep(50400)
    return fourteen_hours


async def in_fifteen_hours():
    fifteen_hours = await asyncio.sleep(54000)
    return fifteen_hours


async def in_sixteen_hours():
    sixteen_hours = await asyncio.sleep(57600)
    return sixteen_hours


async def in_seventeen_hours():
    seventeen_hours = await asyncio.sleep(61200)
    return seventeen_hours


async def in_eighteen_hours():
    eighteen_hours = await asyncio.sleep(64800)
    return eighteen_hours


async def in_nineteen_hours():
    nineteen_hours = await asyncio.sleep(68400)
    return nineteen_hours


async def in_twenty_hours():
    twenty_hours = await asyncio.sleep(72000)
    return twenty_hours


async def in_twenty_one_hours():
    twenty_one_hours = await asyncio.sleep(75600)
    return twenty_one_hours


async def in_twenty_two_hours():
    twenty_two_hours = await asyncio.sleep(79200)
    return twenty_two_hours


async def in_twenty_three_hours():
    twenty_three_hours = await asyncio.sleep(82800)
    return twenty_three_hours


async def in_twenty_four_hours():
    twenty_four_hours = await asyncio.sleep(86400)
    return twenty_four_hours


# sending timed message functions
# each function represents the time until the message will be sent


def send_in_one_minute():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_one_minute())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_ten_minutes():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_ten_minutes())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twenty_minutes():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twenty_minutes())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_thirty_minutes():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_thirty_minutes())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_forty_minutes():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_fourty_minutes())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_fifty_minutes():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_thifty_minutes())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_one_hour():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_one_hour())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_two_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_two_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())


def send_in_three_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_three_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_four_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_four_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_five_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_five_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_six_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_six_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_seven_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_seven_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_eight_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_eight_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_nine_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_nine_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_ten_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_ten_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_eleven_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_eleven_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twelve_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twelve_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_thirteen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_thirteen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_fourteen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_fourteen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_fifteen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_fifteen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_sixteen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_sixteen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_seventeen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_seventeen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_eighteen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_eighteen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_nineteen_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_nineteen_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twenty_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twenty_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twenty_one_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twenty_one_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twenty_two_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twenty_two_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twenty_three_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twenty_three_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


def send_in_twenty_four_hours():
    user = Client(entry_session.get(), entry_api_id.get(), entry_api_hash.get(),
                  proxy=dict(hostname=entry_hostname.get(), port=entry_port.get()))
    user.start()
    asyncio.run(in_twenty_four_hours())
    user.send_message(receiver_user_entry.get(), message_entry.get())
    return


# The program's buttons

register_button = Button(app, text="save info", command=save_info, width=12).grid(row=6, column=0, sticky=W)

message_button = Button(app, text="send message", command=send_a_message, width=12)\
    .grid(row=4, column=2, sticky=W)

message_no_proxy_button = Button(app, text="send message without a proxy", command=send_a_message_no_proxy, width=25)\
    .grid(row=4, column=3, sticky=W)

image_button = Button(app, text="send image", command=send_an_image, width=12).grid(row=5, column=2, sticky=W)

sticker_button = Button(app, text="send sticker", command=send_a_sticker, width=12) \
    .grid(row=6, column=2, sticky=W)

create_group_button = Button(app, text="create group", command=create_group, width=12) \
    .grid(row=13, column=0, sticky=W)

invitation_button1 = Button(app, text="invite 2 users to group", command=invite_2_users_to_group, width=20) \
    .grid(row=17, column=0, sticky=W)

invitation_button2 = Button(app, text="invite 3 users to group", command=invite_3_users_to_group, width=20) \
    .grid(row=18, column=0, sticky=W)

invitation_button3 = Button(app, text="invite 4 users to group", command=invite_4_users_to_group, width=20) \
    .grid(row=19, column=0, sticky=W)

invitation_button4 = Button(app, text="invite 5 users to group", command=invite_5_users_to_group, width=20) \
    .grid(row=20, column=0, sticky=W)

invitation_button5 = Button(app, text="invite 6 users to group", command=invite_6_users_to_group, width=20) \
    .grid(row=21, column=0, sticky=W)

invitation_button6 = Button(app, text="invite 7 users to group", command=invite_7_users_to_group, width=20) \
    .grid(row=22, column=0, sticky=W)

invitation_button7 = Button(app, text="invite 8 users to group", command=invite_8_users_to_group, width=20) \
    .grid(row=23, column=0, sticky=W)

invitation_button8 = Button(app, text="invite 9 users to group", command=invite_9_users_to_group, width=20) \
    .grid(row=24, column=0, sticky=W)

invitation_button9 = Button(app, text="invite 10 users to group", command=invite_10_users_to_group, width=20) \
    .grid(row=25, column=0, sticky=W)

send_message_1_minute = Button(app, text="send message in 1 minute", command=send_in_one_minute, width=30) \
    .grid(row=8, column=2, sticky=W)

send_message_10_minutes = Button(app, text="send message in 10 minutes", command=send_in_ten_minutes, width=30) \
    .grid(row=9, column=2, sticky=W)

send_message_20_minutes = Button(app, text="send message in 20 minutes", command=send_in_twenty_minutes,
                                 width=30).grid(row=10, column=2, sticky=W)

send_message_30_minutes = Button(app, text="send message in 30 minutes", command=send_in_thirty_minutes,
                                 width=30).grid(row=11, column=2, sticky=W)

send_message_40_minutes = Button(app, text="send message in 40 minutes", command=send_in_forty_minutes, width=30) \
    .grid(row=12, column=2, sticky=W)

send_message_50_minutes = Button(app, text="send message in 50 minutes", command=send_in_fifty_minutes, width=30) \
    .grid(row=13, column=2, sticky=W)

send_message_1_hour = Button(app, text="send message in 1 hour", command=send_in_one_hour, width=30) \
    .grid(row=14, column=2, sticky=W)

send_message_2_hours = Button(app, text="send message in 2 hours", command=send_in_two_hours, width=30) \
    .grid(row=15, column=2, sticky=W)

send_message_3_hours = Button(app, text="send message in 3 hours", command=send_in_three_hours, width=30) \
    .grid(row=16, column=2, sticky=W)

send_message_4_hours = Button(app, text="send message in 4 hours", command=send_in_four_hours, width=30) \
    .grid(row=17, column=2, sticky=W)

send_message_5_hours = Button(app, text="send message in 5 hours", command=send_in_five_hours, width=30) \
    .grid(row=18, column=2, sticky=W)

send_message_6_hours = Button(app, text="send message in 6 hours", command=send_in_six_hours, width=30) \
    .grid(row=19, column=2, sticky=W)

send_message_7_hours = Button(app, text="send message in 7 hours", command=send_in_seven_hours, width=30) \
    .grid(row=20, column=2, sticky=W)

send_message_8_hours = Button(app, text="send message in 8 hours", command=send_in_eight_hours, width=30) \
    .grid(row=21, column=2, sticky=W)

send_message_9_hours = Button(app, text="send message in 9 hours", command=send_in_nine_hours, width=30) \
    .grid(row=22, column=2, sticky=W)

send_message_10_hours = Button(app, text="send message in 10 hours", command=send_in_ten_hours, width=30) \
    .grid(row=23, column=2, sticky=W)

send_message_11_hours = Button(app, text="send message in 11 hours", command=send_in_eleven_hours, width=30) \
    .grid(row=24, column=2, sticky=W)

send_message_12_hours = Button(app, text="send message in 12 hours", command=send_in_twelve_hours, width=30) \
    .grid(row=25, column=2, sticky=W)

send_message_13_hours = Button(app, text="send message in 13 hours", command=send_in_thirteen_hours, width=30) \
    .grid(row=8, column=3, sticky=W)

send_message_14_hours = Button(app, text="send message in 14 hours", command=send_in_fourteen_hours, width=30) \
    .grid(row=9, column=3, sticky=W)

send_message_15_hours = Button(app, text="send message in 15 hours", command=send_in_fifteen_hours, width=30) \
    .grid(row=10, column=3, sticky=W)

send_message_16_hours = Button(app, text="send message in 16 hours", command=send_in_sixteen_hours, width=30) \
    .grid(row=11, column=3, sticky=W)

send_message_17_hours = Button(app, text="send message in 17 hours", command=send_in_seventeen_hours, width=30) \
    .grid(row=12, column=3, sticky=W)

send_message_18_hours = Button(app, text="send message in 18 hours", command=send_in_eighteen_hours, width=30) \
    .grid(row=13, column=3, sticky=W)

send_message_19_hours = Button(app, text="send message in 19 hours", command=send_in_nineteen_hours, width=30) \
    .grid(row=14, column=3, sticky=W)

send_message_20_hours = Button(app, text="send message in 20 hours", command=send_in_twenty_hours, width=30) \
    .grid(row=15, column=3, sticky=W)

send_message_21_hours = Button(app, text="send message in 21 hours", command=send_in_twenty_one_hours, width=30) \
    .grid(row=16, column=3, sticky=W)

send_message_22_hours = Button(app, text="send message in 22 hours", command=send_in_twenty_two_hours, width=30) \
    .grid(row=17, column=3, sticky=W)

send_message_23_hours = Button(app, text="send message in 23 hours", command=send_in_twenty_three_hours, width=30) \
    .grid(row=18, column=3, sticky=W)

send_message_24_hours = Button(app, text="send message in 24 hours", command=send_in_twenty_four_hours, width=30) \
    .grid(row=19, column=3, sticky=W)

app.mainloop()
