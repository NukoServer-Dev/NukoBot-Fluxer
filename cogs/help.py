import fluxer

class HelpCog(fluxer.Cog):
    def __init__(self, bot: fluxer.Bot):
        super().__init__(bot)

        self.HELP_SESSIONS = []

    def build_embed(self, emoji: str, is_edit: bool):
        if emoji == "👜":
            embed = fluxer.Embed(title="ロールパネル", description="""`!.rp create <title> <emoji> <role_id>`
ロールパネルを作成します。

`!.rp add <message_id> <emoji> <role_id>`
ロールパネルにロールを追加します。

`!.rp remove <message_id> <role_id>`
ロールパネルからロールを削除します。
""", color=5793266)
        elif emoji == "🔨":
            embed = fluxer.Embed(title="AutoMod", description="""`!.automod create <automod_id>`
AutoModを作成します。

`!.automod delete <automod_id>`
AutoModを削除します。

`!.automod punishment <count> <action>`
<count>回目に処罰された場合、<action>を実行するように設定します。
> 現在は、`send_message`, `none`が<action>に指定できます。

`!.automod punishments`
処罰回数リストを表示します。

`!.clear_warn <user_id>`
警告をクリアします。

> <automod_id>には、現在`invite` `discord_invite`が指定できます。
""", color=5793266)
        elif emoji == "😆":
            embed = fluxer.Embed(title="楽しい", description="""`!.fox`
狐の画像を表示します。

`!.choyen <top> <down>`
5000兆円ほしい！を生成します。

`!.reencode <text>`
文字化けさせます。
""", color=5793266)
        elif emoji == "🔍":
            embed = fluxer.Embed(title="検索", description="""`!.userinfo <userid>`
指定したユーザーの情報を表示します。
""", color=5793266)
        else:
            embed = fluxer.Embed(title="SharkBotのヘルプ", description="""`!.help (引数なし)`
このメッセージを表示します。

👜 ロールパネルを作成するコマンドを知ります。
🔨 AutoModや、処罰関連の設定をするコマンドを知ります。
🔍 検索などができるコマンドを知ります。
😆 面白い機能とコマンドを知ります。
""", color=5793266)

        if is_edit:
            embed = embed.to_dict()

        return embed

    @fluxer.Cog.command(name="help")
    async def help_command(self, msg: fluxer.Message):
        message = await msg.reply(embed=self.build_embed("🏠", False))
        self.HELP_SESSIONS.append(message.id)

        await message.add_reaction("🏠")
        await message.add_reaction("👜")
        await message.add_reaction("🔨")
        await message.add_reaction("🔍")
        await message.add_reaction("😆")

    @fluxer.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add_help(self, reaction_info: fluxer.models.reaction.RawReactionActionEvent):
        if reaction_info.message_id not in self.HELP_SESSIONS:
            return

        if reaction_info.user_id == self.bot.user.id:
            return

        emoji = reaction_info.emoji.unicode

        channel = await self.bot.fetch_channel(reaction_info.channel_id)
        message = await channel.fetch_message(reaction_info.message_id)

        embed = self.build_embed(emoji, True)
        await message.edit(embeds=[embed])

        await message.clear_reactions()

        self.HELP_SESSIONS.remove(reaction_info.message_id)

async def setup(bot: fluxer.Bot):
    await bot.add_cog(HelpCog(bot))

async def teardown(bot: fluxer.Bot):
    await bot.remove_cog(HelpCog(bot).__class__.__name__)