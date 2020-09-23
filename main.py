#!/usr/bin/env python3
"""This module contains the OwOifier bot, which owoifies other people's
messages."""

from re import sub
from random import randint, choice
import discord

client = discord.Client()

faces = ("owo", "òwó", "ówò", "ºwº", "OwO", "ÒwÓ", "ÓwÒ", "oωo", "òωó", "óωò",
         "ºωº", "OωO", "ÒωÓ", "ÓωÒ", "uwu", "ùwú", "úwù", "uωu", "ùωú", "úωù",
         "UwU", "ÙwÚ", "ÚwÙ", "UωU", "ÙωÚ", "ÚωÙ", "·w·", "(·w·)", "(·ω·)",
         ";;w;;", ";;ω;;", ">w<", ">ω<", "≥w≤", "≥ω≤", "^w^", "^ω^", "ǭwǭ",
         "ǭωǭ", "^-^", "(≧∇≦)", "(´·ω·`)")


@client.event
async def on_ready():
    """Lets you know when the bot starts."""
    print(f"Discord version: {discord.__version__}")
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    """Resopnds when someone else sends a message."""
    if message.author == client.user:
        return
    if randint(0, 10) == 0:
        txt = message.content
        txt = sub("(?:r|l)", "w", txt)
        txt = sub("(?:R|L)", "W", txt)
        txt = sub("([nN])([aeiouAEIOU])", "\\1y\\2", txt)
        txt.replace("ove", "uv")
        txt = sub("\\!", f" {choice(faces)}", txt)
        await message.channel.send(txt)


def main():
    """Runs the bot with the token from the file called 'token'."""
    with open("token") as token_file:
        token = token_file.read()
    client.run(token)


if __name__ == "__main__":
    main()
