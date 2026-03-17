"""Pydantic models for Nritya."""
from __future__ import annotations
from pydantic import BaseModel, Field
from enum import Enum


class DanceForm(str, Enum):
    BHARATANATYAM = "Bharatanatyam"
    KATHAK = "Kathak"
    ODISSI = "Odissi"
    KUCHIPUDI = "Kuchipudi"
    MOHINIYATTAM = "Mohiniyattam"


class JointAngle(BaseModel):
    joint_name: str
    angle_degrees: float
    tolerance: float = 10.0


class DancePose(BaseModel):
    name: str
    dance_form: DanceForm
    description: str
    joint_angles: list[JointAngle] = Field(default_factory=list)
    category: str = ""
    difficulty: str = "intermediate"
    tips: str = ""


class MudraType(str, Enum):
    ASAMYUTA = "Asamyuta"  # Single-hand
    SAMYUTA = "Samyuta"    # Double-hand


class Mudra(BaseModel):
    name: str
    sanskrit_name: str
    mudra_type: MudraType
    description: str
    fingers: str
    usage: list[str] = Field(default_factory=list)
    viniyoga: str = ""


class Adavu(BaseModel):
    name: str
    dance_form: DanceForm
    description: str
    steps: list[str] = Field(default_factory=list)
    count_pattern: str = ""
    jathi: str = ""
    difficulty: str = "beginner"


class Expression(BaseModel):
    name: str
    sanskrit_name: str
    description: str
    facial_elements: str = ""


class PoseCorrection(BaseModel):
    joint_name: str
    current_angle: float
    target_angle: float
    deviation: float
    suggestion: str
    severity: str = "minor"


class DanceAnalysis(BaseModel):
    pose_name: str
    dance_form: DanceForm
    overall_score: float
    corrections: list[PoseCorrection] = Field(default_factory=list)
    feedback: str = ""
