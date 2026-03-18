import os
import logging
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation, openai

from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools import get_weather, search_web

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)-22s %(message)s",
)



from dotenv import load_dotenv
import logging

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    noise_cancellation,
    openai as lk_openai,   # 👈 LiveKit OpenAI plugin
)

from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools import get_weather, search_web

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)-22s %(message)s",
)

class Assistant(Agent):
    def __init__(self) -> None:
        # ❗ Now we only set instructions + tools here, NOT llm
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            tools=[get_weather, search_web],
        )


async def entrypoint(ctx: agents.JobContext):
    # ✅ Realtime model handles STT + LLM + TTS
    session = AgentSession(
        llm=lk_openai.realtime.RealtimeModel(
            # model left as default "gpt-realtime"
            voice="alloy",      # or any OpenAI voice you like
            temperature=0.8,
        ),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION,
    )


if __name__== "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
