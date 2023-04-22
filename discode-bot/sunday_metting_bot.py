import discord
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, time, timedelta
from pytz import timezone
from dotenv import load_dotenv


load_dotenv()
sunday_api = os.environ.get("SUNDAY_METTING_API")
sunday_channel_id = os.environ.get("SUNDAY_CHANNEL_ID")

print("sunday_api: ", sunday_api)
print("sunday_channel_id: ", sunday_channel_id)

TOKEN = sunday_api
intents = discord.Intents.default()
client = discord.Client(intents=intents)
print("client: ", client)

scheduler = AsyncIOScheduler()  # APScheduler 스케줄러 생성


# 일요일 9시 30분 (KST)로 스케줄링
@scheduler.scheduled_job(
    "cron", day_of_week="sun", hour=9, minute=30, second=0, timezone="Asia/Seoul"
)
async def scheduled_message():
    await client.wait_until_ready()
    channel = client.get_channel(int(sunday_channel_id))  # 알림을 보낼 디스코드 채널 ID 입력
    await channel.send(
        "@everyone 매주 일요일 10시에 #라운지 에서 회의가 있습니다. 참석해주세요!"
    )  # 알림 메시지 내용 입력


async def send_notification():
    await client.wait_until_ready()
    channel = client.get_channel(int(sunday_channel_id))
    print(channel)
    await channel.send("마지막 메시지 도착!")


@client.event
async def on_ready():
    print(f"{client.user}로 로그인하였습니다.")
    print(client.user.id)

    start_time = datetime.now(timezone("Asia/Seoul")) + timedelta(minutes=1)
    scheduler.add_job(send_notification, "date", run_date=start_time)

    scheduler.start()


client.run(TOKEN)
