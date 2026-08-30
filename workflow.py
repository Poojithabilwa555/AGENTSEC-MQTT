from langgraph.graph import StateGraph, START, END

from agent_state import AgentState

from agents.supervisor import supervisor_agent
from agents.mqtt_agent import mqtt_agent
from agents.log_agent import log_agent
from agents.ml_agent import ml_agent
from agents.auth_agent import auth_agent
from agents.investigation_agent import investigation_agent
from agents.risk_agent import risk_agent
from agents.response_agent import response_agent


def build_workflow():

    graph = StateGraph(AgentState)

    # -------------------------------------------------
    # Add agents
    # -------------------------------------------------

    graph.add_node(
        "supervisor",
        supervisor_agent
    )

    graph.add_node(
        "mqtt",
        mqtt_agent
    )

    graph.add_node(
        "logs",
        log_agent
    )

    graph.add_node(
        "ml",
        ml_agent
    )

    graph.add_node(
        "auth",
        auth_agent
    )

    graph.add_node(
        "investigation",
        investigation_agent
    )

    graph.add_node(
        "risk",
        risk_agent
    )

    graph.add_node(
        "response",
        response_agent
    )

    # -------------------------------------------------
    # Workflow connections
    # -------------------------------------------------

    graph.add_edge(
        START,
        "supervisor"
    )

    # Supervisor sends the event
    # to the analysis agents.

    graph.add_edge(
        "supervisor",
        "mqtt"
    )

    graph.add_edge(
        "supervisor",
        "logs"
    )

    graph.add_edge(
        "supervisor",
        "ml"
    )

    graph.add_edge(
        "supervisor",
        "auth"
    )

    # All analysis agents continue
    # to the investigation stage.

    graph.add_edge(
        "mqtt",
        "investigation"
    )

    graph.add_edge(
        "logs",
        "investigation"
    )

    graph.add_edge(
        "ml",
        "investigation"
    )

    graph.add_edge(
        "auth",
        "investigation"
    )

    # Investigation → Risk

    graph.add_edge(
        "investigation",
        "risk"
    )

    # Risk → Response

    graph.add_edge(
        "risk",
        "response"
    )

    # Response → END

    graph.add_edge(
        "response",
        END
    )

    return graph.compile()