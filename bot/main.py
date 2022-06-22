import os
import discord
from discord.ext import commands
from run_selector import select_weekly_runs

arboretum = {
    3: '//snippets.mapmycdn.com/routes/view/embedded/380811542?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    5: '//snippets.mapmycdn.com/routes/view/embedded/380811742?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    7: '//snippets.mapmycdn.com/routes/view/embedded/380812136?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
}

bridge = {
    3: '//mapmyfitness.com/routes/view/embedded/5061837349?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
    5: '//mapmyfitness.com/routes/view/embedded/5061841969?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
    7: '//mapmyfitness.com/routes/view/embedded/5061843712?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined'
}

gasworks = {
    3: '//mapmyfitness.com/routes/view/embedded/5061816547?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
    5: '//mapmyfitness.com/routes/view/embedded/5061828625?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined',
    7: '//mapmyfitness.com/routes/view/embedded/5061830644?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined'
}

green_lake = {
    3: '//snippets.mapmycdn.com/routes/view/embedded/381215294?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    5: '//snippets.mapmycdn.com/routes/view/embedded/381216728?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    7: '//snippets.mapmycdn.com/routes/view/embedded/381218394?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
}

interlaken = {
    3: '//snippets.mapmycdn.com/routes/view/embedded/356639835?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    5: '//snippets.mapmycdn.com/routes/view/embedded/380810830?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    7: '//snippets.mapmycdn.com/routes/view/embedded/380811260?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
}

laurelhurst = {
    3: '//snippets.mapmycdn.com/routes/view/embedded/380812480?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    5: '//snippets.mapmycdn.com/routes/view/embedded/380812908?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    7: '//snippets.mapmycdn.com/routes/view/embedded/380813832?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
}

ravenna = {
    3: '//snippets.mapmycdn.com/routes/view/embedded/1362222805?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2016-11-17T22:15:40-08:00',
    5: '//snippets.mapmycdn.com/routes/view/embedded/381208242?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00',
    7: '//snippets.mapmycdn.com/routes/view/embedded/381213640?width=600&height=400&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2014-03-29T17:09:05-05:00'
}

long_names = {
    1: '//snippets.mapmycdn.com/routes/view/embedded/1379987599?width=600&height=400&&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2016-12-06T00:45:07-08:00',
    2: '//snippets.mapmycdn.com/routes/view/embedded/2865761827?width=600&height=400&&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2020-01-18T18:57:46-08:00',
    3: '//snippets.mapmycdn.com/routes/view/embedded/2730969919?width=600&height=400&&line_color=E60f0bdb&rgbhex=DB0B0E&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2019-10-13T21:00:38-07:00',
    4: '//mapmyfitness.com/routes/view/embedded/5050970416?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&last_updated=2022-06-13T21:16:51+00:00'
}

long_names_converted = {
    1: 'Capitol Hill',
    2: 'Green Lake Zoo Loop',
    3: 'Infamous Zoo Loop',
    4: 'Magnuson Park'
}

long_names_converted_reversed = {
    'Capitol Hill': 1,
    'Green Lake Zoo Loop': 2,
    'Infamous Zoo Loop': 3,
    'Magnuson Park': 4
}

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command(name="weekly")
@commands.has_role("Officer")
async def ping(ctx):
    weekly_runs = select_weekly_runs()
    f_run = weekly_runs[4]
    friday_run = long_names_converted[f_run]
    weekly_runs[4] = friday_run
    with open('weekly_runs.txt', 'w') as f:
        for index in range(len(weekly_runs) - 1):
            run = weekly_runs[index].capitalize()
            if run == "Green_lake":
                run = "Green Lake"
            if run == "Bridge":
                run = "520 Bridge"
            f.write(run)
            f.write('\n')
            weekly_runs[index] = run
    with open('index.txt', 'w') as f:
        f.write("0")
    await ctx.send(weekly_runs)

@bot.command(name="daily")
@commands.has_role("Officer")
async def ping(ctx):
    index = 0
    with open('index.txt', 'r') as f:
        index = f.readlines()[0]
        index = int(index)
    with open('index.txt', 'w') as f:
        f.write(index + 1)
    if index < 5:
        with open('weekly_runs.txt', 'r') as f:
            await ctx.send(f.readlines()[index])
    else:
        await ctx.send("Error. Only 5 weekdays.")
    #embed=discord.Embed(title="Green Lake Zoo Loop", url="https://www.mapmyfitness.com/routes/view/embedded/5050970416?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined'",
    #description="Test Embed", color=0xFF5733)
    #file = discord.File("imgs/long_names/Green_Lake_Zoo_Loop.png", filename="Green_Lake_Zoo_Loop.png")
    #embed.set_thumbnail(url="attachment://Green_Lake_Zoo_Loop.png")
    #await ctx.send(file=file, embed=embed)

@bot.command(name="index")
@commands.has_role("Officer")
async def ping(ctx):
    try:
        with open('index.txt', 'r') as f:
            await ctx.send(f.readlines()[0])
    except:
        with open('index.txt', 'w') as f:
            f.write("0")
        with open('index.txt', 'r') as f:
            await ctx.send(f.readlines()[0])

if __name__ == "__main__":
    bot.run(TOKEN)
