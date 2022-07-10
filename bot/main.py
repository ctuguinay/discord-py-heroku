import os
import discord
from discord.ext import commands
from run_selector import select_weekly_runs
import pytest
import argparse

dict = {

    "Arboretum": {
        3: '//snippets.mapmycdn.com/routes/view/embedded/380811542?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        5: '//snippets.mapmycdn.com/routes/view/embedded/380811742?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        7: '//snippets.mapmycdn.com/routes/view/embedded/380812136?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
    },

    "520 Bridge": {
        3: '//mapmyfitness.com/routes/view/embedded/5061837349?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
        5: '//mapmyfitness.com/routes/view/embedded/5061841969?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
        7: '//mapmyfitness.com/routes/view/embedded/5061843712?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined'
    },

    "Gasworks": {
        3: '//mapmyfitness.com/routes/view/embedded/5061816547?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
        5: '//mapmyfitness.com/routes/view/embedded/5061828625?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
        7: '//mapmyfitness.com/routes/view/embedded/5061830644?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined'
    },

    "Green Lake": {
        3: '//snippets.mapmycdn.com/routes/view/embedded/381215294?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        5: '//snippets.mapmycdn.com/routes/view/embedded/381216728?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        7: '//snippets.mapmycdn.com/routes/view/embedded/381218394?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
    },

    "Interlaken": {
        3: '//snippets.mapmycdn.com/routes/view/embedded/356639835?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        5: '//snippets.mapmycdn.com/routes/view/embedded/380810830?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        7: '//snippets.mapmycdn.com/routes/view/embedded/380811260?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
    },

    "Laurelhurst": {
        3: '//snippets.mapmycdn.com/routes/view/embedded/380812480?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        5: '//snippets.mapmycdn.com/routes/view/embedded/380812908?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        7: '//snippets.mapmycdn.com/routes/view/embedded/380813832?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
    },

    "Ravenna": {
        3: '//snippets.mapmycdn.com/routes/view/embedded/1362222805?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2016-11-17T22:15:40-08:00',
        5: '//snippets.mapmycdn.com/routes/view/embedded/381208242?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
        7: '//snippets.mapmycdn.com/routes/view/embedded/381213640?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
    }
}

long_names = {
    'Capitol Hill': '//snippets.mapmycdn.com/routes/view/embedded/2730969919?width=600&height=400&&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2019-10-13T21:00:38-07:00',
    'Green Lake Zoo Loop': '//mapmyfitness.com/routes/view/embedded/5050970416?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2022-06-13T21:16:51+00:00',
    'Infamous Lake Union Loop': '//snippets.mapmycdn.com/routes/view/embedded/1379987599?width=600&height=400&&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2016-12-06T00:45:07-08:00',
    'Magnuson Park': '//snippets.mapmycdn.com/routes/view/embedded/2865761827?width=600&height=400&&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2020-01-18T18:57:46-08:00'
}

# Parser to parse whether you are running through local or through Heroku
parser = argparse.ArgumentParser(description='Parser for Husky Running Club Discord Bot.')
parser.add_argument("--set_mode", help="Sets whether you are running locally or through heroku.", default="locally")
args = parser.parse_args()
mode = args.set_mode

if mode == "locally":
    from dotenv import load_dotenv
    load_dotenv()

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    channel = bot.get_channel(990343297329397820)

@bot.command(name="initialize")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    with open('bot/weekly_index.txt', 'w') as f:
        f.write("0")
    await channel.send("Initialized Quarter.")

@bot.command(name="weekly")
@commands.has_role("Officer")
async def ping(ctx):
    try:
        channel = bot.get_channel(990343297329397820)
        weekly_runs = select_weekly_runs()
        with open('bot/weekly_runs.txt', 'w') as f:
            for index in range(len(weekly_runs)):
                run = weekly_runs[index]
                if run == "Bridge":
                    run = "520 Bridge"
                f.write(run)
                f.write('\n')
                weekly_runs[index] = run
        with open('bot/weekday_index.txt', 'w') as f:
            f.write("0")
        with open('bot/weekly_index.txt', 'r') as f:
            weekly_index = f.readlines()[0]
            weekly_index = int(weekly_index)
        with open('bot/weekly_index.txt', 'w') as f:
            weekly_next_index = weekly_index + 1
            weekly_next_index = str(weekly_next_index)
            f.write(weekly_next_index)
        await channel.send("**Here is our Week " + weekly_next_index + " Run Schedule:**")
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for index in range(len(weekly_runs)):
            run = weekly_runs[index]
            weekday = weekdays[index]
            await channel.send(weekday + ": " + run)
        embed=discord.Embed(title="Husky Running Club Routes", url="https://dawgs.run/routes/",
        description="You can view all our routes here.", color=0xFF5733)
        file = discord.File("bot/imgs/hrc_logo.jpg", filename="hrc_logo.jpg")
        embed.set_thumbnail(url="attachment://hrc_logo.jpg")
        await channel.send(file=file, embed=embed)
    except:
        await channel.send("Error. Have not initialized bot for the quarter.")

@bot.command(name="daily")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        with open('bot/weekday_index.txt', 'r') as f:
            index = f.readlines()[0]
            index = int(index)
        with open('bot/weekday_index.txt', 'w') as f:
            next_index = index + 1
            next_index = str(next_index)
            f.write(next_index)
        if index < 5:
            with open('bot/weekly_runs.txt', 'r') as f:
                run = f.readlines()[index]
                run = run.replace("\n", "")
                underscore = run.replace(" ", "_")
                if index != 1 and index != 4:
                    message_one = "**Today's run is " + run + "!**"
                    message_two = "Be at the Quad by 5:00pm"
                    message_three = "Here are links to maps of the different distances we will run:"
                    await channel.send(message_one)
                    await channel.send(message_two)
                    await channel.send(message_three)
                    for mile in [3,5,7]:
                        link = dict[run][3]
                        path_append = "bot/imgs/" + underscore + "/"
                        path = underscore + "_" + str(mile) + ".png"
                        embed=discord.Embed(title=run, url="https:" + link,
                        description="Map Link for " + run + " " + str(mile) + " route.", color=0xFF5733)
                        file = discord.File(path_append + path, filename=path)
                        embed.set_thumbnail(url="attachment://" + path)
                        await channel.send(file=file, embed=embed)
                elif index == 1:
                    message_one = "**Today is a " + run + " day!**"
                    message_two = "Be at the Quad at 5:30pm. We will jog to Roosevelt from there together."
                    await channel.send(message_one)
                    await channel.send(message_two)
                elif index == 4:
                    message_one = "**Today's long run is " + run + "!**"
                    message_two = "Be at the Quad by 5:00pm."
                    message_three = "Here is the link to the map of the run:"
                    await channel.send(message_one)
                    await channel.send(message_two)
                    await channel.send(message_three)
                    link = long_names[run]
                    path_append = "bot/imgs/long_names/"
                    path = underscore + ".png"
                    embed=discord.Embed(title=run, url="https:" + link,
                    description="Map Link for " + run + " route.", color=0xFF5733)
                    file = discord.File(path_append + path, filename=path)
                    embed.set_thumbnail(url="attachment://" + path)
                    await channel.send(file=file, embed=embed)
                    await channel.send("*Note: Since this is a fairly long run, feel free to turn back whenever.*")

        else:
            await channel.send("Error. Only 5 weekdays.")
    except:
        await channel.send("Error. Did not set weekly runs.")

@bot.command(name="weekly_index")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        with open('bot/weekly_index.txt', 'r') as f:
            await channel.send("Weekly Index: " + f.readlines()[0])
    except:
        with open('bot/weekly_index.txt', 'w') as f:
            f.write("0")
        with open('bot/weekly_index.txt', 'r') as f:
            await channel.send("Weekly Index: " + f.readlines()[0])

@bot.command(name="weekday_index")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        with open('bot/weekday_index.txt', 'r') as f:
            await channel.send("Weekday Index: " + f.readlines()[0])
    except:
        with open('bot/weekday_index.txt', 'w') as f:
            f.write("0")
        with open('bot/weekday_index.txt', 'r') as f:
            await channel.send("Weekday Index: " + f.readlines()[0])

@bot.command(name="set_weekly_index")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        weekly_index = ctx.message.content.replace("!set_weekly_index ", "")
        with open('bot/weekly_index.txt', 'w') as f:
            f.write(weekly_index)
            await channel.send("Set weekly index to: " + weekly_index)
    except:
        await channel.send("Error. Try: !set_weekly_index int")

@bot.command(name="set_weekday_index")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        weekday_index = ctx.message.content.replace("!set_weekday_index ", "")
        with open('bot/weekday_index.txt', 'w') as f:
            f.write(weekday_index)
            await channel.send("Set weekday index to: " + weekday_index)
    except:
        await channel.send("Error. Try: !set_weekday_index int")

@bot.command(name="backup_weekly_runs")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        with open('bot/weekly_runs.txt', 'r') as f, open('bot/backup_weekly_runs.txt', 'w') as w:
            for index in range(5):
                run = f.readline()
                w.write(run)
        await channel.send("Backed up weekly runs.")
    except:
        await channel.send("Error. Weekly runs have not been initialized.")

@bot.command(name="use_backup_weekly_runs")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    try:
        with open('bot/backup_weekly_runs.txt', 'r') as f, open('bot/weekly_runs.txt', 'w') as w:
            for index in range(5):
                run = f.readline()
                w.write(run)
        await channel.send("Using backedup weekly runs.")
    except:
        await channel.send("Error. Backup weekly runs have not been initialized.")

@bot.command(name="shutdown")
@commands.has_role("Officer")
async def ping(ctx):
    channel = bot.get_channel(990343297329397820)
    await channel.send("Bot logging off.")
    await bot.logout()

if __name__ == "__main__":
    bot.run(TOKEN)
    channel = bot.get_channel(990343297329397820)
