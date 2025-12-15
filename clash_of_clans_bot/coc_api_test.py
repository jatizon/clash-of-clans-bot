import asyncio
import coc
from dotenv import load_dotenv
import os

load_dotenv()

COC_API_KEY = os.getenv("COC_API_KEY")
COC_DEV_LOGIN = os.getenv("COC_DEV_LOGIN")
COC_DEV_PASSWORD = os.getenv("COC_DEV_PASSWORD")

try:
    COC_SEARCH_LIMIT = int(os.getenv("COC_SEARCH_LIMIT", "5"))
except ValueError:
    COC_SEARCH_LIMIT = 5


async def main():
    async with coc.Client() as coc_client:
        try:
            await coc_client.login(COC_DEV_LOGIN, COC_DEV_PASSWORD)
        except coc.InvalidCredentials as error:
            exit(error)

        player = await coc_client.get_player("GYOV2PLVQ")
        print(f"{player.name} has {player.trophies} trophies!")

        clans = await coc_client.search_clans(name="best clan ever", limit=5)
        for clan in clans:
            print(f"{clan.name} ({clan.tag}) has {clan.member_count} members")

        try:
            war = await coc_client.get_current_war("#clantag")
            print(f"{war.clan_tag} is currently in {war.state} state.")
        except:
            pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass