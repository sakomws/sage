import asyncio
from datetime import datetime
import json
import logging
from typing import Optional
from livekit import agents, rtc
from livekit.plugins import openai, silero

import prompt_runner as prompt_runner

class GCSAI:
    @classmethod
    async def create(cls, ctx: agents.JobContext):
        agent = GCSAI(ctx)
        await agent.start()

    def __init__(self, ctx: agents.JobContext):
        # plugins
        self.whisper_stt = openai.STT()
        self.vad = silero.VAD()
        self.dalle = openai.Dalle3()

        self.ctx = ctx
        self.chat = rtc.ChatManager(ctx.room)
        self.prompt: Optional[str] = None
        self.current_image: Optional[rtc.VideoFrame] = None

        # setup callbacks
        def subscribe_cb(
            track: rtc.Track,
            publication: rtc.TrackPublication,
            participant: rtc.RemoteParticipant,
        ):
            self.ctx.create_task(self.audio_track_worker(track))

        def process_chat(msg: rtc.ChatMessage):
            self.prompt = msg.message

        self.ctx.room.on("track_subscribed", subscribe_cb)
        self.chat.on("message_received", process_chat)

    async def start(self):
        # give a bit of time for the user to fully connect so they don't miss
        # the welcome message
        await asyncio.sleep(1)

        # create_task is used to run coroutines in the background
        self.ctx.create_task(
            self.chat.send_message(
                "I am your GCS Assistant! How can I help you today?"
            )
        )

        self.ctx.create_task(self.text_generation_worker())
        self.update_agent_state("listening")

    def update_agent_state(self, state: str):
        metadata = json.dumps(
            {
                "agent_state": state,
            }
        )
        self.ctx.create_task(self.ctx.room.local_participant.update_metadata(metadata))

    async def audio_track_worker(self, track: rtc.Track):
        audio_stream = rtc.AudioStream(track)
        vad_stream = self.vad.stream(min_silence_duration=2.0)
        stt = agents.stt.StreamAdapter(self.whisper_stt, vad_stream)
        stt_stream = stt.stream()
        self.ctx.create_task(self.stt_worker(stt_stream))

        async for audio_frame_event in audio_stream:
            stt_stream.push_frame(audio_frame_event.frame)
        await stt_stream.flush()

    async def stt_worker(self, stt_stream: agents.stt.SpeechStream):
        async for event in stt_stream:
            # we only want to act when result is final
            if not event.is_final:
                continue
            speech = event.alternatives[0]
            self.prompt = speech.text
        await stt_stream.aclose()

    async def text_generation_worker(self):
        # task will be canceled when Agent is disconnected
        while True:
            prompt, self.prompt = self.prompt, None
            if prompt:
                self.update_agent_state("generating")
                self.ctx.create_task(
                    self.chat.send_message(
                        f'Loading GCSAI for: "{prompt}"'
                    )
                )
                started_at = datetime.now()
                try:
                   reply=prompt_runner.get_query_from_user(prompt)
                   print("HERE IS RESPONSE:",reply)
                   self.ctx.create_task(
                            self.chat.send_message(f'"{reply}"')
                    )
                except Exception as e:
                    logging.error("failed to generate image: %s", e, exc_info=e)
                    self.ctx.create_task(
                        self.chat.send_message("Sorry, I ran into an error.")
                    )
                self.update_agent_state("listening")
            await asyncio.sleep(0.05)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    async def job_request_cb(job_request: agents.JobRequest):
        await job_request.accept(
            GCSAI.create,
            identity="GCSAI",
            name="GCSAI",
            # subscribe to all audio tracks automatically
            auto_subscribe=agents.AutoSubscribe.AUDIO_ONLY,
            # disconnect when the last participant leaves
            auto_disconnect=agents.AutoDisconnect.DEFAULT,
        )

    worker = agents.Worker(request_handler=job_request_cb)
    agents.run_app(worker)