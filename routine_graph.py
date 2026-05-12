import yaml
from typing import TypedDict, Optional, Dict, Any, List

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openrouter import ChatOpenRouter

from neo4j import GraphDatabase

load_dotenv()

# Helper function to load routine.yaml
def load_routine(path: str):
    with open(path, "r") as file:
        return yaml.safe_load(file)
    
routine = load_routine("routine.yaml")

llm = ChatOpenRouter(
    model="openai/gpt-4o-mini",
    temperature=0.3,
)

class TutorState(TypedDict):
    routine: Dict[str, Any]
    current_step_id: str
    learner_message: str
    tutor_message: str
    route: Optional[str]
    history: List[Dict[str, str]]

def get_current_step(state: TutorState):
    

def tutor_node(state: TutorState):
    """
    Get's the curr
    """
    step = state["current_step_id"]
    tutor_message = step["prompt"]

    return {
        "tutor_message": tutor_message,
        "current_step_id": step["next"],
        "history": step["history"] + [{"role": "tutor", "content": tutor_message}]
    }






