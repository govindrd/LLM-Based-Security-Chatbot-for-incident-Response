from typing import Any

from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    name: str
    args: dict[str, Any] = Field(default_factory=dict)


class TraceStep(BaseModel):
    step_id: str
    agent: str
    rationale: str
    outputs: dict[str, Any]
    tool_calls: list[ToolCall] = Field(default_factory=list)
    policy_hits: list[str] = Field(default_factory=list)
    confidence: float = 0.6


class FinalDecision(BaseModel):
    summary: str
    risk_score: float
    recommendations: list[str]


class ConversationResult(BaseModel):
    steps: list[TraceStep]
    final: FinalDecision
