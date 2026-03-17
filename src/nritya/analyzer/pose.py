"""PoseAnalyzer comparing dance pose to reference."""
from __future__ import annotations
import numpy as np
from ..models import DancePose, JointAngle, PoseCorrection, DanceAnalysis


class PoseAnalyzer:
    """Analyze a dancer's pose against reference poses using joint angles."""

    def analyze(self, reference: DancePose, observed_angles: dict[str, float]) -> DanceAnalysis:
        """Compare observed joint angles against a reference dance pose.

        Args:
            reference: The ideal reference pose with target angles.
            observed_angles: Dict mapping joint_name to observed angle in degrees.

        Returns:
            DanceAnalysis with score and corrections.
        """
        corrections: list[PoseCorrection] = []
        deviations: list[float] = []

        for ref_angle in reference.joint_angles:
            if ref_angle.joint_name not in observed_angles:
                continue
            observed = observed_angles[ref_angle.joint_name]
            deviation = abs(observed - ref_angle.angle_degrees)
            deviations.append(deviation)

            if deviation > ref_angle.tolerance:
                severity = "minor" if deviation <= ref_angle.tolerance * 2 else "major"
                direction = "increase" if observed < ref_angle.angle_degrees else "decrease"
                corrections.append(PoseCorrection(
                    joint_name=ref_angle.joint_name,
                    current_angle=observed,
                    target_angle=ref_angle.angle_degrees,
                    deviation=deviation,
                    suggestion=f"{direction.capitalize()} {ref_angle.joint_name} angle by {deviation:.1f} degrees",
                    severity=severity,
                ))

        # Calculate overall score (100 = perfect)
        if deviations:
            avg_deviation = float(np.mean(deviations))
            max_possible = 180.0
            overall_score = max(0.0, 100.0 * (1.0 - avg_deviation / max_possible))
        else:
            overall_score = 0.0

        feedback = self._generate_feedback(corrections, overall_score)
        return DanceAnalysis(
            pose_name=reference.name,
            dance_form=reference.dance_form,
            overall_score=round(overall_score, 1),
            corrections=corrections,
            feedback=feedback,
        )

    def _generate_feedback(self, corrections: list[PoseCorrection], score: float) -> str:
        if score >= 95:
            return "Excellent! Your pose is nearly perfect."
        elif score >= 85:
            return f"Very good! Minor adjustments needed in {len(corrections)} joint(s)."
        elif score >= 70:
            return f"Good effort. Focus on correcting {len(corrections)} alignment(s)."
        elif score >= 50:
            return f"Needs improvement. {len(corrections)} significant corrections needed."
        else:
            return "Keep practicing. Focus on the fundamental position first."

    def compute_similarity(self, pose_a: dict[str, float], pose_b: dict[str, float]) -> float:
        """Compute similarity between two sets of joint angles (0-100)."""
        common_joints = set(pose_a.keys()) & set(pose_b.keys())
        if not common_joints:
            return 0.0
        diffs = [abs(pose_a[j] - pose_b[j]) for j in common_joints]
        avg_diff = float(np.mean(diffs))
        return max(0.0, 100.0 * (1.0 - avg_diff / 180.0))
