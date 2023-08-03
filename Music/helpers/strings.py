ᴏclass TEXTS:
    ABOUT_SONG = (
        "**💬 Title:** __{0}__ \n\n"
        "**📺 Channel:** __{1}__ \n"
        "**🕰 Published:** __{2}__ \n"
        "**🔖 Views:** __{3}__ \n"
        "**⏳ Duration:** __{4}__ \n\n"
        "**❆** {5}"
    )
    ABOUT_USER = (
        "**✘ Top User Info:**\n\n"
        "**💬 Name:** {0}\n"
        "**💠 ID:** `{1}`\n"
        "**⚜️ Level:** __{2}__\n"
        "**🎶 Songs Played:** __{3}__\n"
        "**〥 Joined Since:** __{4}__\n\n"
        "**❆** {5}"
    )
    BOOTED = (
        "#START\n\n"
        "**{0} is alive!**\n\n"
        "__» ᴊᴀɴᴠɪ-Music Version:__ `{1}`\n"
        "__» Python Version:__ `{2}`\n"
        "__» Pyrogram Version:__ `{3}`\n"
        "__» PyTgCalls Version:__ `{4}`\n\n"
        "**</>** {5}"
    )
    PING_REPLY = (
        "**📌 Pinged Bot Server!**\n\n"
        "**🏁 Speed:** __{0} ms__\n"
        "**⏳ Uptime:** __{1}__\n"
        "**🎶 VC Ping:** __{2} ms__"
    )
    PLAYING = (
        "**❆
            ┏━━━━━━━━━━━━━━━━⧫
            ┠ 🀄 Sᴛᴀʀᴛᴇᴅ Pʟᴀʏɪɴɢ°
            ┗━━━━━━━━━━━━━━━━⧫** {0}\n\n"
        "**➻sᴏɴɢ💫** __{1}__\n"
        "**◆ 
            ╰ ᴅᴜʀᴀᴛɪᴏɴ »** __{2}__\n"
        "**◆ 
            ╰ Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ »** {3}"
    )
    PROFILE = (
        "**{0}\nUser Profile**\n\n"
        "**💬 Name:** {1}\n"
        "**💠 ID:** `{2}`\n"
        "**📝 User Type:** __{3}__\n"
        "**⚜️ Level:** __{4}__\n"
        "**🎶 Songs Played:** __{5}__\n"
        "**〥 Joined Since:** __{6}__\n\n"
        "**❆** {7}"
    )
    QUEUE = (
        "** ┏━━━━━━━━━━━━━━━━⧫
            ┠ 🀄 Aᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ °
            ┗━━━━━━━━━━━━━━━━⧫(#{0})** \n\n"
        "**➻sᴏɴɢ💫:** __{1}__\n"
        "**◆ 
            ╰ ᴅᴜʀᴀᴛɪᴏɴ »** __{2}__\n"
        "**◆ 
            ╰ ǫᴜᴇᴜᴇᴅ ʙʏ »** {3}"
    )
    SONG_CAPTION = (
        "**⊸ ᴛɪᴛʟᴇ:** [{0}]({1})\n\n"
        "**⊸ ᴠɪᴇᴡs:** {2}\n"
        "**⊸ ᴅᴜʀᴀᴛɪᴏɴ:** {3}\n"
        "**⊸ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {4}\n\n"
        "**❆** {5}"
    )
    SOURCE = (
        "**Source 📦:**\n\n"
        "**Note:** \n__» The source code is available on GitHub. You can find the link below.__\n"
        "__» Every project available under The-HellBot are open-source and free to use and modify to your needs.__\n"
        "__» Anyone pretending to be the developer of this bot and selling the code, is a scammer.__\n\n"
        "__» Please consider giving a star to the repository if you liked the project.__\n"
        "__» Feel free to contact us if you need any help regarding the source code.__\n\n"
        "❤️🎶 {0}"
    )
    STATS = (
        "**⤞ Server Stats:**\n"
        "    __Total Users:__ `{0} users`\n"
        "    __Total Chats:__ `{1} chats`\n"
        "    __Total Gbans:__ `{2} users`\n"
        "    __Blocked Users:__ `{3} users`\n"
        "    __Songs Played:__ `{4} songs`\n"
        "    __Active VC:__ `{5} vc`\n\n"
        "**⤞ System Stats:**\n"
        "    __Core:__ `{6} cores`\n"
        "    __CPU Usage:__ `{7}`\n"
        "    __Disk Usage:__ `{8}`\n"
        "    __RAM Usage:__ `{9}`\n"
        "    __Uptime:__ `{10}`\n\n"
        "**</>** {11}"
    )
    SYSTEM = (
        "**⤞ System Info:**\n\n"
        "   __Core:__ `{0} cores`\n"
        "   __CPU Usage:__ `{1}`\n"
        "   __Disk Usage:__ `{2}`\n"
        "   __RAM Usage:__ `{3}`\n"
        "   __Uptime:__ `{4}`\n\n"
        "**</>** {5}"
    )
    HELP_ADMIN = (
        "**Aᴜᴛʜ Usᴇʀ Cᴍᴅs:**\n\n"
        "**» /auth ; /unauth**\n"
        "    __Authorize or unauthorize user to use admins command such as /skip, /pause, etc.__\n\n"
        "**» /authlist**\n"
        "    __List all authorized users.__\n\n"
        "**» /authchat**\n"
        "    __This enables all the users in the chat to use admins command such as /skip, /pause, etc.__\n\n"
        "**» /mute ; /unmute**\n"
        "    __Mute or unmute the ongoing track in the voice chat.__\n\n"
        "**» /pause ; /resume**\n"
        "    __Pause or resume the ongoing track in the voice chat.__\n\n"
        "**» /stop ; /end**\n"
        "    __Stop the ongoing track in the voice chat.__\n\n"
        "**» /loop**\n"
        "    __Loop the playing track in the voice chat. Use [/loop 0] to disable the loop.__\n\n"
        "**» /skip**\n"
        "    __Skip the playing track in the voice chat.__\n\n"
        "**» /replay**\n"
        "    __Replay from the beginning of the playing track in the voice chat.__\n\n"
        "**» /seek**\n"
        "    __Seek the playing track in the voice chat. Use [/seek 10] to seek forward and [/seek-10] to seek backwards.__\n\n"
        "**» /clean**\n"
        "    __Clear the queue when bot seems to be bugged.__\n\n"
    )
    HELP_USER = (
        "**ɴᴏʀᴍᴀʟ ᴜsᴇʀ.ᴄᴍᴅs:**\n\n"
        "**» /play ; /vplay**\n"
        "    __Play replied audio/video file or youtube video or searched query on voice chat.__\n\n"
        "**» /fplay ; /fvplay**\n"
        "    __Force play replied audio/video file or youtube video or searched query on voice chat.__\n\n"
        "**» /favs ; /myfavs ; /favorites**\n"
        "    __Show your favorite songs list.__\n\n"
        "**» /delfavs**\n"
        "    __Delete your favorite songs from your list.__\n\n"
        "**» /current ; /playing**\n"
        "    __Show the current playing song.__\n\n"
        "**» /queue ; /que ; /q**\n"
        "    __Show the queued songs list.__\n\n"
        "**» /song**\n"
        "    __Download the searched song from youtube.__\n\n"
        "**» /lyrics**\n"
        "    __Get the lyrics of the searched song. Give artist name after ' - ' for accurate results. [/lyrics Without Me - Eminem]__\n\n"
        "**» /profile ; /me**\n"
        "    __Show your profile and stats.__\n\n"
    )
    HELP_SUDO = (
        "**Sᴜᴅᴏ:**\n\n"
        "**» /active**\n"
        "    __Check active voice chats of the bot.__\n\n"
        "**» /autoend**\n"
        "    __Enable or disable autoend inactive voice chats.__\n\n"
        "**» /block ; /unblock**\n"
        "    __Block or unblock user from using the bot.__\n\n"
        "**» /blocklist**\n"
        "    __List all blocked users.__\n\n"
        "**» /gban ; /ungban**\n"
        "    __Globally ban or unban user from using the bot.__\n\n"
        "**» /gbanlist**\n"
        "    __List all globally banned users.__\n\n"
        "**» /logs**\n"
        "    __Get the logs of the bot.__\n\n"
        "**» /restart**\n"
        "    __Restart the bot globally.__\n\n"
        "**» /sudolist**\n"
        "    __List all sudo users.__\n\n"
        "**» /stats**\n"
        "    __Show full stats of the bot.__\n\n"
    )
    HELP_OTHERS = (
        "**Oᴛʜᴇʀ:**\n\n"
        "**» /start**\n"
        "    __Check if the bot is alive.__\n\n"
        "**» /ping**\n"
        "    __Check ping of the bot.__\n\n"
        "**» /help**\n"
        "    __Show this menu.__\n\n"
        "**» /sysinfo**\n"
        "    __Show system information of the bot.__\n\n"
        "**» /leaderboard ; /topusers**\n"
        "    __Show the top 10 users with most number of songs played.__\n\n"
    )
    HELP_OWNERS = (
        "**Oᴡɴᴇʀ:**\n\n"
        "**» /eval ; /run**\n"
        "    __Execute the python script.__\n\n"
        "**» /exec ; /term ; /sh**\n"
        "    __Execute the bash script.__\n\n"
        "**» /getvar ; /gvar ; /var**\n"
        "    __Get the value of the config variable.__\n\n"
        "**» /addsudo**\n"
        "    __Add sudo user of the bot who can use sudo commands.__\n\n"
        "**» /rmsudo ; /delsudo**\n"
        "    __Remove sudo user of the bot.__\n\n"
    )
    HELP_GC = (
        "Get the help menu in your PM. "
        "__Click the button below!__"
    )
    HELP_PM = (
        "**Hᴇʟᴘ⚙**\n\n"
        "__» All commands are categorized based on their usability and target users.__\n"
        "__» You can use these buttons below to navigate each category and get respective commands.__\n"
        "__» Feel free to contact us if you need any help regarding the bot.__\n\n"
        "❤️🎶 {0}"
    )
    START_GC = (
        "ʏᴇᴀʜ, ɪ ᴀᴍ ᴀʟɪᴠᴇ !</> "
        "__ᴘʟᴀʏ sᴏᴍᴇᴛʜɪɴɢ ɪɴᴛʀᴇsᴛɪɴɢ<!>?__"
    )
    START_PM = (
        "**Hɪᴇ** {0}**!**\n\n"
        "**ɪ ,ᴀᴍ** {1} **, ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴄ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ᴀᴍᴀᴢɪɴɢ ғᴇᴀᴛᴜʀᴇs .**\n"
        "**𝙰ᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ !**\n\n"
        "__➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs</>!__\n"
        "__➻ ғᴇᴇʟ ᴛʜᴇ ᴍᴜsɪᴄ ᴠɪʙᴇs ᴀɴᴅ ᴇɴᴏᴊʏ ᴡɪᴛʜ ʏᴏᴜʀ ғʀɪᴇɴᴅs...__\n\n"
        "≧◉◡◉≦ᴍᴀᴅᴇ ʙʏ sᴜᴍɪᴛ  @{2}"
    )
    PERFORMER = "[ ᴛʜᴇ sᴜᴍɪᴛ  ]"
