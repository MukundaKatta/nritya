"""DanceCorrector generating alignment corrections."""
from __future__ import annotations
from ..models import DancePose, DanceAnalysis, PoseCorrection, DanceForm
from .pose import PoseAnalyzer
from ..dance.poses import DancePoseLibrary


class DanceCorrector:
    """Generate detailed alignment corrections for dance poses."""

    def __init__(self) -> None:
        self.analyzer = PoseAnalyzer()
        self.library = DancePoseLibrary()
        self._correction_tips: dict[str, dict[str, str]] = {
            "left_knee": {
                "increase": "Straighten your left leg more. Push the knee back gently.",
                "decrease": "Bend your left knee deeper. Ensure it tracks over your toes.",
            },
            "right_knee": {
                "increase": "Straighten your right leg more. Engage your quadriceps.",
                "decrease": "Bend your right knee deeper. Keep weight centered.",
            },
            "spine": {
                "increase": "Straighten your spine. Imagine a string pulling from your crown.",
                "decrease": "You are leaning back slightly. Bring your torso vertical.",
            },
            "hip_tilt": {
                "increase": "Push your hip further to the side for a deeper deflection.",
                "decrease": "Reduce your hip tilt. Keep more centered.",
            },
            "torso_bend": {
                "increase": "Bend your upper body more to create the S-curve.",
                "decrease": "Reduce your torso bend. Keep it subtler.",
            },
            "neck_tilt": {
                "increase": "Tilt your head more toward your deflected hip.",
                "decrease": "Reduce your head tilt. Keep it gentle and natural.",
            },
            "left_shoulder": {
                "increase": "Raise your left arm higher to shoulder level.",
                "decrease": "Lower your left arm slightly. Avoid tension in the shoulder.",
            },
            "right_shoulder": {
                "increase": "Raise your right arm higher.",
                "decrease": "Lower your right arm. Keep it relaxed but controlled.",
            },
        }

    def correct_pose(self, pose_name: str, observed_angles: dict[str, float]) -> DanceAnalysis | None:
        """Analyze and correct a named pose given observed angles."""
        reference = self.library.get_pose(pose_name)
        if reference is None:
            return None
        analysis = self.analyzer.analyze(reference, observed_angles)
        # Enrich corrections with detailed tips
        for correction in analysis.corrections:
            direction = "decrease" if correction.current_angle > correction.target_angle else "increase"
            joint_tips = self._correction_tips.get(correction.joint_name, {})
            tip = joint_tips.get(direction)
            if tip:
                correction.suggestion = tip
        return analysis

    def find_closest_pose(self, observed_angles: dict[str, float], dance_form: DanceForm | None = None) -> tuple[DancePose, float]:
        """Find the closest matching reference pose to observed angles."""
        poses = self.library.get_poses_by_form(dance_form) if dance_form else self.library.get_all_poses()
        best_pose = poses[0]
        best_score = 0.0
        for pose in poses:
            ref_angles = {a.joint_name: a.angle_degrees for a in pose.joint_angles}
            score = self.analyzer.compute_similarity(ref_angles, observed_angles)
            if score > best_score:
                best_score = score
                best_pose = pose
        return best_pose, best_score

    def get_practice_sequence(self, dance_form: DanceForm, difficulty: str = "beginner") -> list[DancePose]:
        """Get a recommended practice sequence for a given form and difficulty."""
        poses = [p for p in self.library.get_poses_by_form(dance_form) if p.difficulty == difficulty]
        if not poses:
            poses = self.library.get_poses_by_form(dance_form)
        return poses
