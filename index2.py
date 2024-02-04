import openai
import urllib
import os
import base64
import speech_recognition as sr


openai.api_key = ""


ZyntriQix_remote_filepath = "https://cdn.openai.com/API/examples/data/ZyntriQix.wav"
ZyntriQix_filepath = "data/ZyntriQix.wav"


urllib.request.urlretrieve(ZyntriQix_remote_filepath, ZyntriQix_filepath)

def transcribe(prompt: str, audio_filepath) -> str:
    """Given a prompt, transcribe the audio file."""
  
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_filepath) as source:
        audio_data = recognizer.record(source)
    
    text_transcription = recognizer.recognize_google(audio_data)
    
  
    transcript = openai.Completion.create(
        model="davinci-002",
        prompt=f"{prompt}\n{text_transcription}",
        temperature=0.7,
        max_tokens=200,
    )

    return transcript.choices[0].text.strip()


transcription_result = transcribe(prompt="", audio_filepath=ZyntriQix_filepath)
print(transcription_result) 
transcribe(
    prompt="ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T.",
    audio_filepath=ZyntriQix_filepath,
)
transcribe(
    prompt="ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, AstroPixel Array, QuantumFlare Five, CyberPulse Six, VortexDrive Matrix, PhotonLink Ten, TriCircuit Array, PentaSync Seven, UltraWave Eight, QuantumVertex Nine, HyperHelix X, DigiSpiral Z, PentaQuark Eleven, TetraCube Twelve, GigaPhase Thirteen, EchoNeuron Fourteen, FusionPulse V15, MetaQuark Sixteen, InfiniCircuit Seventeen, TeraPulse Eighteen, ExoMatrix Nineteen, OrbiSync Twenty, QuantumHelix TwentyOne, NanoPhase TwentyTwo, TeraFractal TwentyThree, PentaHelix TwentyFour, ExoCircuit TwentyFive, HyperQuark TwentySix, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T.",
    audio_filepath=ZyntriQix_filepath,
)

def transcribe_with_spellcheck(system_message, audio_filepath):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": transcribe(prompt="", audio_filepath=audio_filepath),
            },
        ],
    )
    return completion.choices[0].message.content

system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T."
new_text = transcribe_with_spellcheck(system_prompt, audio_filepath=ZyntriQix_filepath)
print(new_text)

system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array,  OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, AstroPixel Array, QuantumFlare Five, CyberPulse Six, VortexDrive Matrix, PhotonLink Ten, TriCircuit Array, PentaSync Seven, UltraWave Eight, QuantumVertex Nine, HyperHelix X, DigiSpiral Z, PentaQuark Eleven, TetraCube Twelve, GigaPhase Thirteen, EchoNeuron Fourteen, FusionPulse V15, MetaQuark Sixteen, InfiniCircuit Seventeen, TeraPulse Eighteen, ExoMatrix Nineteen, OrbiSync Twenty, QuantumHelix TwentyOne, NanoPhase TwentyTwo, TeraFractal TwentyThree, PentaHelix TwentyFour, ExoCircuit TwentyFive, HyperQuark TwentySix, GigaLink TwentySeven, FusionMatrix TwentyEight, InfiniFractal TwentyNine, MetaSync Thirty, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."
new_text = transcribe_with_spellcheck(system_prompt, audio_filepath=ZyntriQix_filepath)
print(new_text)

system_prompt = "You are a helpful assistant for the company ZyntriQix. Your first task is to list the words that are not spelled correctly according to the list provided to you and to tell me the number of misspelled words. Your next task is to insert those correct words in place of the misspelled ones. List: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array,  OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, AstroPixel Array, QuantumFlare Five, CyberPulse Six, VortexDrive Matrix, PhotonLink Ten, TriCircuit Array, PentaSync Seven, UltraWave Eight, QuantumVertex Nine, HyperHelix X, DigiSpiral Z, PentaQuark Eleven, TetraCube Twelve, GigaPhase Thirteen, EchoNeuron Fourteen, FusionPulse V15, MetaQuark Sixteen, InfiniCircuit Seventeen, TeraPulse Eighteen, ExoMatrix Nineteen, OrbiSync Twenty, QuantumHelix TwentyOne, NanoPhase TwentyTwo, TeraFractal TwentyThree, PentaHelix TwentyFour, ExoCircuit TwentyFive, HyperQuark TwentySix, GigaLink TwentySeven, FusionMatrix TwentyEight, InfiniFractal TwentyNine, MetaSync Thirty, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T."
new_text = transcribe_with_spellcheck(system_prompt, audio_filepath=ZyntriQix_filepath)
print(new_text)

