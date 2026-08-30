from langgraph.graph import StateGraph, START, END

from graph.state import SecurityState

from agents.supervisor import supervisor_agent
from agents.mqtt_agent import mqtt_agent
from agents.log_agent import log_agent
from agents.threat_intel_agent import threat_intel_agent
from agents.investigation_agent import investigation_agent
from agents.risk_agent import risk_agent
from agents.response_agent import response_agent


def route_from_supervisor(state):

    selected_agents = state.get(
        "selected_agents",
        []
    )

    if selected_agents:

        return selected_agents[0]

    return "log_agent"


def route_after_mqtt(state):

    return "log_agent"


def build_workflow():

    graph = StateGraph(
        SecurityState
    )

    # -----------------------------
    # Add agents
    # -----------------------------

    graph.add_node(
        "supervisor",
        supervisor_agent
    )

    graph.add_node(
        "mqtt_agent",
        mqtt_agent
    )

    graph.add_node(
        "log_agent",
        log_agent
    )

    graph.add_node(
        "threat_intel_agent",
        threat_intel_agent
    )

    graph.add_node(
        "investigation_agent",
        investigation_agent
    )

    graph.add_node(
        "risk_agent",
        risk_agent
    )

    graph.add_node(
        "response_agent",
        response_agent
    )

    # -----------------------------
    # START
    # -----------------------------

    graph.add_edge(
        START,
        "supervisor"
    )

    # -----------------------------
    # Supervisor routing
    # -----------------------------

    graph.add_conditional_edges(

        "supervisor",

        route_from_supervisor,

        {
            "mqtt_agent": "mqtt_agent",

            "log_agent": "log_agent"
        }
    )

    # -----------------------------
    # MQTT → Log
    # -----------------------------

    graph.add_edge(
        "mqtt_agent",
        "log_agent"
    )

    # -----------------------------
    # Log → Threat Intelligence
    # -----------------------------

    graph.add_edge(
        "log_agent",
        "threat_intel_agent"
    )

    # -----------------------------
    # Threat Intelligence
    # → Investigation
    # -----------------------------

    graph.add_edge(
        "threat_intel_agent",
        "investigation_agent"
    )

    # -----------------------------
    # Investigation → Risk
    # -----------------------------

    graph.add_edge(
        "investigation_agent",
        "risk_agent"
    )

    # -----------------------------
    # Risk → Response
    # -----------------------------

    graph.add_edge(
        "risk_agent",
        "response_agent"
    )

    # -----------------------------
    # Response → END
    # -----------------------------

    graph.add_edge(
        "response_agent",
        END
    )

    return graph.compile()