import fluxer

class UserInfoCog(fluxer.Cog):
    def __init__(self, bot: fluxer.Bot):
        super().__init__(bot)

    def make_userinfo_embed(self, user: fluxer.User):
        embed = fluxer.Embed(title=f"{user.username}#{user.discriminator}の情報", color=5793266)
        embed.add_field(name="ID", value=str(user.id))
        embed.add_field(name="グローバル名", value=str(user.global_name))
        embed.add_field(name="作成日", value=str(user.created_at))
        embed.set_thumbnail(url=user.avatar_url)
        return embed

    @fluxer.Cog.command(name="userinfo")
    async def help_command(self, msg: fluxer.Message):
        split_message = msg.content.split()
        if len(split_message) < 2:
            await msg.send(embed=self.make_userinfo_embed(msg.author))
            return

        userid = split_message[1]
        try:
            user = await self.bot.fetch_user(userid)
            await msg.send(embed=self.make_userinfo_embed(user))
        except:
            await msg.send("❌️不明なユーザーかもしれない")

    @fluxer.Cog.command(name="whoami")
    async def whoami_command(self, msg: fluxer.Message):
        try:
            await msg.send(embed=self.make_userinfo_embed(msg.author))
        except:
            await msg.send("❌️不明なユーザーかもしれない")

async def setup(bot: fluxer.Bot):
    await bot.add_cog(UserInfoCog(bot))

async def teardown(bot: fluxer.Bot):
    await bot.remove_cog(UserInfoCog(bot).__class__.__name__)