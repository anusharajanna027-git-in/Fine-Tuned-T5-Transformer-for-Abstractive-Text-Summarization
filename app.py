#fast API
from fastapi import FastAPI, Request
from pydantic import BaseModel
# recreate the same libraries when during used in building the model
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# initialize our fast api app using FastAPI()fnx
app = FastAPI(title="Text Summarizer App", description="Text Summarizer using T5", version="1.0")

#to load our model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

#lets specify our device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
model.to(device)

#templating
templates = Jinja2Templates(directory=".")

# define the input schema means input formate which is in string formate=>str
# to define formate we have BaseModel and we create a class for on  which the dialogue will come
class DialogueInput(BaseModel):
    dialogue: str

# define the clean_data function
def clean_data(text):
    text = re.sub(r"\r\n", " ", text) # lines of next lines existed in the data 
    text = re.sub(r"\s+", " ", text) # to remove the extra spaces=>\s+ becomes the std code for to remove the extra spaces 
    text = re.sub(r"<.*?>", " ", text)  # to remove the html tags
    text = text.strip().lower() # remove the extra spaces and converted text into lowercase
    return text

# define the summarization function=>core logic
def summerize_dialogue(dialogue: str):
    #we clean the dialogue =>use clean_data()fnx
    dialogue = clean_data(dialogue)
    #tokenize the dialogues
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length = 512,
        truncation=True,
        return_tensors="pt"
    )

    # generate the summary=>tokens id's
    
    targets = model.generate(
        input_ids = inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # token ids converted to text=>decoding by using  tokenizer
    summary = tokenizer.decode(targets[0],skip_special_tokens=True)
    return summary
    

# crate API Endpoints using FastAPI
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summerize_dialogue(dialogue_input.dialogue)
    return {"summary": summary}

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")