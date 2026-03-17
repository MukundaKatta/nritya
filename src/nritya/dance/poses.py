"""DancePoseLibrary with 30+ poses and correct joint angles."""
from __future__ import annotations
from ..models import DancePose, DanceForm, JointAngle


class DancePoseLibrary:
    """Library of 30+ classical dance poses with reference joint angles."""

    def __init__(self) -> None:
        self._poses: list[DancePose] = self._load_poses()

    def _load_poses(self) -> list[DancePose]:
        return [
            # Bharatanatyam poses
            DancePose(name="Aramandi", dance_form=DanceForm.BHARATANATYAM,
                      description="Half-sitting position - fundamental stance",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=110, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=110, tolerance=10),
                          JointAngle(joint_name="left_hip", angle_degrees=110, tolerance=10),
                          JointAngle(joint_name="right_hip", angle_degrees=110, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Keep spine erect. Knees point outward over toes. Weight evenly distributed."),
            DancePose(name="Muzhumandi", dance_form=DanceForm.BHARATANATYAM,
                      description="Full-sitting position - deep squat",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=60, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=60, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="stance", difficulty="intermediate",
                      tips="Full squat with spine straight. Heels may lift slightly."),
            DancePose(name="Samapadam", dance_form=DanceForm.BHARATANATYAM,
                      description="Equal standing position - feet together",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="right_knee", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Stand straight, feet together, arms at sides."),
            DancePose(name="Nataraja Pose", dance_form=DanceForm.BHARATANATYAM,
                      description="Lord Shiva's cosmic dance pose - one leg raised",
                      joint_angles=[
                          JointAngle(joint_name="standing_knee", angle_degrees=160, tolerance=10),
                          JointAngle(joint_name="raised_knee", angle_degrees=90, tolerance=15),
                          JointAngle(joint_name="raised_hip", angle_degrees=90, tolerance=15),
                          JointAngle(joint_name="right_elbow", angle_degrees=90, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="iconic", difficulty="advanced",
                      tips="Standing leg slightly bent. Raised foot at knee height. One arm in Abhaya, other in Gaja hasta."),
            DancePose(name="Mandala Stance", dance_form=DanceForm.BHARATANATYAM,
                      description="Wide stance with deep bend",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=100, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=100, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="stance", difficulty="intermediate",
                      tips="Wider than Aramandi, deeper bend. Feet turned out fully."),
            DancePose(name="Swastika Standing", dance_form=DanceForm.BHARATANATYAM,
                      description="Crossed-leg standing pose",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=170, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=170, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="transition", difficulty="beginner",
                      tips="One foot crossed in front of the other. Arms in Swastika mudra."),
            DancePose(name="Prerana", dance_form=DanceForm.BHARATANATYAM,
                      description="One leg extended sideways, body tilted",
                      joint_angles=[
                          JointAngle(joint_name="standing_knee", angle_degrees=120, tolerance=10),
                          JointAngle(joint_name="extended_knee", angle_degrees=170, tolerance=10),
                          JointAngle(joint_name="torso_tilt", angle_degrees=15, tolerance=5),
                      ],
                      category="extension", difficulty="intermediate",
                      tips="Extend one leg to the side with pointed foot. Tilt torso slightly opposite."),
            DancePose(name="Alidha", dance_form=DanceForm.BHARATANATYAM,
                      description="Warrior-like lunge pose",
                      joint_angles=[
                          JointAngle(joint_name="front_knee", angle_degrees=90, tolerance=10),
                          JointAngle(joint_name="back_knee", angle_degrees=170, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=175, tolerance=5),
                      ],
                      category="dynamic", difficulty="intermediate",
                      tips="Deep lunge with back leg straight. Front knee over ankle."),
            DancePose(name="Garudamandala", dance_form=DanceForm.BHARATANATYAM,
                      description="Eagle-spread pose with arms wide",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=110, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=110, tolerance=10),
                          JointAngle(joint_name="left_shoulder", angle_degrees=90, tolerance=10),
                          JointAngle(joint_name="right_shoulder", angle_degrees=90, tolerance=10),
                      ],
                      category="expressive", difficulty="intermediate",
                      tips="Aramandi with both arms spread wide like eagle wings."),
            DancePose(name="Urdhva Janu", dance_form=DanceForm.BHARATANATYAM,
                      description="Raised knee pose",
                      joint_angles=[
                          JointAngle(joint_name="standing_knee", angle_degrees=170, tolerance=10),
                          JointAngle(joint_name="raised_knee", angle_degrees=45, tolerance=15),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="balance", difficulty="intermediate",
                      tips="Raise one knee high toward chest. Keep standing leg firm."),

            # Kathak poses
            DancePose(name="Sama", dance_form=DanceForm.KATHAK,
                      description="Basic standing position of Kathak",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="right_knee", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=3),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Stand perfectly straight, feet together, one hand at waist, other in Pataka."),
            DancePose(name="Kathak Tribhangi", dance_form=DanceForm.KATHAK,
                      description="Three-bend pose in Kathak style",
                      joint_angles=[
                          JointAngle(joint_name="hip_tilt", angle_degrees=15, tolerance=5),
                          JointAngle(joint_name="torso_bend", angle_degrees=10, tolerance=5),
                          JointAngle(joint_name="neck_tilt", angle_degrees=15, tolerance=5),
                      ],
                      category="expressive", difficulty="intermediate",
                      tips="Subtle S-curve. Less dramatic than Odissi tribhangi. Grace and poise."),
            DancePose(name="Chakkar Preparation", dance_form=DanceForm.KATHAK,
                      description="Preparation stance before spinning",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=175, tolerance=5),
                          JointAngle(joint_name="right_knee", angle_degrees=175, tolerance=5),
                          JointAngle(joint_name="right_arm", angle_degrees=90, tolerance=10),
                      ],
                      category="preparation", difficulty="intermediate",
                      tips="Weight on balls of feet. Arms positioned for momentum. Eyes fixed on spotting point."),
            DancePose(name="Thumri Pose", dance_form=DanceForm.KATHAK,
                      description="Expressive pose for emotive dance",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=160, tolerance=10),
                          JointAngle(joint_name="hip_tilt", angle_degrees=10, tolerance=5),
                          JointAngle(joint_name="neck_tilt", angle_degrees=20, tolerance=10),
                      ],
                      category="expressive", difficulty="intermediate",
                      tips="Gentle sway, expressive eyes, hand near face in Hamsasya mudra."),
            DancePose(name="Tatkar Stance", dance_form=DanceForm.KATHAK,
                      description="Footwork execution stance",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=175, tolerance=5),
                          JointAngle(joint_name="right_knee", angle_degrees=175, tolerance=5),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=3),
                      ],
                      category="footwork", difficulty="beginner",
                      tips="Stand tall, weight on flat feet. Heels strike ground alternately."),

            # Odissi poses
            DancePose(name="Chauka", dance_form=DanceForm.ODISSI,
                      description="Square stance - masculine energy",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=120, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=120, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="hip_tilt", angle_degrees=0, tolerance=3),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Feet apart, knees out. Spine perfectly straight. No hip deflection."),
            DancePose(name="Tribhangi", dance_form=DanceForm.ODISSI,
                      description="Three-bend pose - feminine energy, signature of Odissi",
                      joint_angles=[
                          JointAngle(joint_name="hip_tilt", angle_degrees=25, tolerance=10),
                          JointAngle(joint_name="torso_bend", angle_degrees=15, tolerance=5),
                          JointAngle(joint_name="neck_tilt", angle_degrees=20, tolerance=10),
                          JointAngle(joint_name="standing_knee", angle_degrees=160, tolerance=10),
                      ],
                      category="stance", difficulty="intermediate",
                      tips="Deep S-curve through body. Hip pushes strongly to one side. Head tilts to hip side."),
            DancePose(name="Abhanga", dance_form=DanceForm.ODISSI,
                      description="Slight hip deflection pose",
                      joint_angles=[
                          JointAngle(joint_name="hip_tilt", angle_degrees=10, tolerance=5),
                          JointAngle(joint_name="standing_knee", angle_degrees=170, tolerance=5),
                          JointAngle(joint_name="spine", angle_degrees=175, tolerance=5),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Subtle hip shift. Less extreme than Tribhangi. Weight on one leg."),
            DancePose(name="Samabhanga", dance_form=DanceForm.ODISSI,
                      description="Symmetrical standing pose",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="right_knee", angle_degrees=180, tolerance=5),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=3),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Perfectly symmetrical. Used for salutation and start/end."),
            DancePose(name="Bhumi Pranam", dance_form=DanceForm.ODISSI,
                      description="Earth salutation - deep forward bend",
                      joint_angles=[
                          JointAngle(joint_name="hip_flexion", angle_degrees=90, tolerance=15),
                          JointAngle(joint_name="left_knee", angle_degrees=180, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=180, tolerance=10),
                      ],
                      category="devotional", difficulty="beginner",
                      tips="Bend from hips touching the ground. Rise gracefully into Tribhangi."),

            # Kuchipudi poses
            DancePose(name="Kuchipudi Aramandi", dance_form=DanceForm.KUCHIPUDI,
                      description="Half-sitting position in Kuchipudi style",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=115, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=115, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=5),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Similar to Bharatanatyam but slightly higher. More dynamic and bouncy."),
            DancePose(name="Plate Dance Balance", dance_form=DanceForm.KUCHIPUDI,
                      description="Balancing on brass plate edges",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=120, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=120, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=3),
                          JointAngle(joint_name="ankle_flexion", angle_degrees=45, tolerance=10),
                      ],
                      category="specialty", difficulty="advanced",
                      tips="Balance on plate rim edges. Feet grip plate edges. Core engaged for stability."),
            DancePose(name="Pot Balance", dance_form=DanceForm.KUCHIPUDI,
                      description="Dancing with pot on head",
                      joint_angles=[
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=2),
                          JointAngle(joint_name="neck", angle_degrees=180, tolerance=2),
                          JointAngle(joint_name="left_knee", angle_degrees=115, tolerance=10),
                      ],
                      category="specialty", difficulty="advanced",
                      tips="Absolute stillness in head and neck. All movement from waist down."),
            DancePose(name="Krishna Pose", dance_form=DanceForm.KUCHIPUDI,
                      description="Lord Krishna playing flute - characteristic Kuchipudi pose",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=160, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=140, tolerance=10),
                          JointAngle(joint_name="hip_tilt", angle_degrees=20, tolerance=10),
                          JointAngle(joint_name="left_elbow", angle_degrees=45, tolerance=10),
                      ],
                      category="character", difficulty="intermediate",
                      tips="Crossed legs, hip tilted. Hands positioned as if holding flute. Playful expression."),

            # Mohiniyattam poses
            DancePose(name="Mohiniyattam Aramandi", dance_form=DanceForm.MOHINIYATTAM,
                      description="Gentle half-sitting in Mohiniyattam",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=130, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=130, tolerance=10),
                          JointAngle(joint_name="spine", angle_degrees=178, tolerance=5),
                      ],
                      category="stance", difficulty="beginner",
                      tips="Softer, higher Aramandi than Bharatanatyam. Gentle sway in body."),
            DancePose(name="Swaying Palm", dance_form=DanceForm.MOHINIYATTAM,
                      description="Signature swaying movement of Mohiniyattam",
                      joint_angles=[
                          JointAngle(joint_name="hip_sway", angle_degrees=15, tolerance=5),
                          JointAngle(joint_name="torso_sway", angle_degrees=10, tolerance=5),
                          JointAngle(joint_name="left_knee", angle_degrees=160, tolerance=10),
                      ],
                      category="movement", difficulty="intermediate",
                      tips="Gentle lateral sway like a coconut palm in breeze. Continuous fluid motion."),
            DancePose(name="Lasya Pose", dance_form=DanceForm.MOHINIYATTAM,
                      description="Graceful feminine expression pose",
                      joint_angles=[
                          JointAngle(joint_name="hip_tilt", angle_degrees=10, tolerance=5),
                          JointAngle(joint_name="neck_tilt", angle_degrees=15, tolerance=10),
                          JointAngle(joint_name="right_elbow", angle_degrees=120, tolerance=10),
                      ],
                      category="expressive", difficulty="intermediate",
                      tips="Soft, rounded movements. Eyes expressive. Hands flow like water."),
            DancePose(name="Cholkettu Opening", dance_form=DanceForm.MOHINIYATTAM,
                      description="Opening invocatory pose",
                      joint_angles=[
                          JointAngle(joint_name="left_knee", angle_degrees=130, tolerance=10),
                          JointAngle(joint_name="right_knee", angle_degrees=130, tolerance=10),
                          JointAngle(joint_name="left_shoulder", angle_degrees=70, tolerance=10),
                          JointAngle(joint_name="right_shoulder", angle_degrees=70, tolerance=10),
                      ],
                      category="invocation", difficulty="beginner",
                      tips="Both hands in Anjali. Gentle sway. Eyes follow hand movement."),

            # Additional poses
            DancePose(name="Anjali (Prayer)", dance_form=DanceForm.BHARATANATYAM,
                      description="Prayer pose with hands joined at chest",
                      joint_angles=[
                          JointAngle(joint_name="spine", angle_degrees=180, tolerance=3),
                          JointAngle(joint_name="elbow_angle", angle_degrees=60, tolerance=10),
                      ],
                      category="devotional", difficulty="beginner",
                      tips="Palms together at chest. Elbows slightly lifted. Serene expression."),
            DancePose(name="Natarajasana (Dance King)", dance_form=DanceForm.BHARATANATYAM,
                      description="Advanced balance pose inspired by Nataraja sculpture",
                      joint_angles=[
                          JointAngle(joint_name="standing_knee", angle_degrees=170, tolerance=10),
                          JointAngle(joint_name="raised_thigh", angle_degrees=90, tolerance=15),
                          JointAngle(joint_name="raised_knee", angle_degrees=90, tolerance=15),
                          JointAngle(joint_name="left_arm_elevation", angle_degrees=90, tolerance=10),
                      ],
                      category="iconic", difficulty="advanced",
                      tips="Balance on one leg. Other leg bent with foot at waist height. Arms in Abhaya and Gaja mudra."),
        ]

    def get_all_poses(self) -> list[DancePose]:
        return self._poses

    def get_poses_by_form(self, form: DanceForm) -> list[DancePose]:
        return [p for p in self._poses if p.dance_form == form]

    def get_pose(self, name: str) -> DancePose | None:
        for p in self._poses:
            if p.name.lower() == name.lower():
                return p
        return None

    def get_poses_by_category(self, category: str) -> list[DancePose]:
        return [p for p in self._poses if p.category == category]

    def get_poses_by_difficulty(self, difficulty: str) -> list[DancePose]:
        return [p for p in self._poses if p.difficulty == difficulty]
