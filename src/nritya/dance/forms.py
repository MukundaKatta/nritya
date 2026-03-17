"""DanceFormDatabase with Bharatanatyam/Kathak/Odissi/Kuchipudi/Mohiniyattam."""
from __future__ import annotations
from ..models import DanceForm, Adavu, Expression


class DanceFormDatabase:
    """Database of classical Indian dance forms with adavus, expressions, and details."""

    def __init__(self) -> None:
        self._adavus: list[Adavu] = self._load_adavus()
        self._expressions: list[Expression] = self._load_expressions()
        self._form_details: dict[DanceForm, dict] = self._load_form_details()

    def _load_form_details(self) -> dict[DanceForm, dict]:
        return {
            DanceForm.BHARATANATYAM: {
                "origin": "Tamil Nadu",
                "style": "Angular, precise movements with emphasis on aramandi (half-sitting position)",
                "key_elements": ["Nritta (pure dance)", "Nritya (expressional)", "Natya (dramatic)"],
                "costume": "Silk saree with fan pleats, temple jewelry, ghungroo",
                "music": "Carnatic music with mridangam, veena, flute",
                "key_positions": ["Aramandi", "Muzhumandi", "Samapadam"],
            },
            DanceForm.KATHAK: {
                "origin": "North India (Lucknow and Jaipur gharanas)",
                "style": "Fluid spins (chakkar), intricate footwork, storytelling through expression",
                "key_elements": ["Tatkar (footwork)", "Chakkar (spins)", "Thumri", "Tarana"],
                "costume": "Anarkali or lehenga, ghungroo (100+ bells)",
                "music": "Hindustani music with tabla, sarangi, sitar",
                "key_positions": ["Sama", "Tribhangi", "Atibhangi"],
            },
            DanceForm.ODISSI: {
                "origin": "Odisha",
                "style": "Sculptural tribhangi (three-bend) pose, fluid and lyrical",
                "key_elements": ["Tribhangi", "Chauka", "Pallavi", "Abhinaya"],
                "costume": "Pattasari (Odia saree style), silver jewelry",
                "music": "Odissi music with mardala, flute, sitar",
                "key_positions": ["Chauka", "Tribhangi", "Abhanga"],
            },
            DanceForm.KUCHIPUDI: {
                "origin": "Andhra Pradesh",
                "style": "Dance-drama tradition with fast rhythmic footwork and dramatic expression",
                "key_elements": ["Jatiswaram", "Shabdam", "Tarangam", "Dance on brass plate"],
                "costume": "Silk saree with pleats, similar to Bharatanatyam",
                "music": "Carnatic music with mridangam, violin, flute",
                "key_positions": ["Aramandi", "Prerana", "Samabhanga"],
            },
            DanceForm.MOHINIYATTAM: {
                "origin": "Kerala",
                "style": "Graceful, feminine, swaying movements like a palm tree",
                "key_elements": ["Lasya (graceful)", "Cholkettu", "Jatiswaram", "Padam"],
                "costume": "White and gold Kerala saree, jasmine flowers in hair",
                "music": "Sopana music style with edakka, flute, veena",
                "key_positions": ["Aramandi", "Swaying stance", "Tribhangi"],
            },
        }

    def _load_adavus(self) -> list[Adavu]:
        return [
            # Bharatanatyam Adavus
            Adavu(name="Tatta Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Basic stamping steps, foundation of Bharatanatyam footwork",
                  steps=["Stand in Aramandi", "Stamp right foot flat", "Stamp left foot flat", "Alternate with rhythm"],
                  count_pattern="Tai Ya Tai Hi", jathi="Tisra (3 counts)", difficulty="beginner"),
            Adavu(name="Natta Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Stretching steps combining arm and leg movements",
                  steps=["Start Aramandi", "Extend right leg sideways", "Right arm in Tripataka", "Return to center", "Repeat left"],
                  count_pattern="Tai Yum Tat Ta", jathi="Chatusra (4 counts)", difficulty="beginner"),
            Adavu(name="Visharu Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Sliding or spreading steps with cross-leg movements",
                  steps=["Aramandi", "Slide right foot out", "Cross left behind", "Arms in Alapadma", "Return"],
                  count_pattern="Tai Ya Tai Hi", jathi="Tisra", difficulty="intermediate"),
            Adavu(name="Tattimetti Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Combination of flat stamps and toe-heel patterns",
                  steps=["Stamp flat right", "Raise on toes", "Drop heels", "Stamp flat left", "Repeat pattern"],
                  count_pattern="Tai Tat Tai Hi Ta Ha", jathi="Misra (7 counts)", difficulty="intermediate"),
            Adavu(name="Tirumanam Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Jumping steps with both feet",
                  steps=["Jump landing in Aramandi", "Stamp right", "Stamp left", "Jump again"],
                  count_pattern="Tat Tai Ta Ha", jathi="Chatusra", difficulty="intermediate"),
            Adavu(name="Murka Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Turning steps with spiral movement",
                  steps=["Start Aramandi", "Step right", "Turn body right", "Complete turn", "End in Aramandi"],
                  count_pattern="Tai Ya Tai Hi", jathi="Chatusra", difficulty="advanced"),
            Adavu(name="Jaru Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Sliding steps with smooth gliding motion",
                  steps=["Aramandi", "Slide right foot smoothly", "Shift weight", "Slide left foot", "Maintain level"],
                  count_pattern="Tai Ya Tai Hi", jathi="Tisra", difficulty="intermediate"),
            Adavu(name="Kudittu Metta Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Jump-stamp combination, energetic adavu",
                  steps=["Jump up from Aramandi", "Stamp right on landing", "Jump again", "Stamp left"],
                  count_pattern="Tai Tat Tai Hi", jathi="Chatusra", difficulty="advanced"),
            Adavu(name="Mandi Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Sitting (full-squat) steps",
                  steps=["Full squat (Muzhumandi)", "Rise to Aramandi", "Extend one leg", "Return to squat"],
                  count_pattern="Tai Ya Tai Hi", jathi="Chatusra", difficulty="advanced"),
            Adavu(name="Sarikkal Adavu", dance_form=DanceForm.BHARATANATYAM,
                  description="Sideways sliding steps with hand gestures",
                  steps=["Aramandi", "Slide right with right hand Pataka", "Bring left foot", "Repeat other side"],
                  count_pattern="Tai Ya Tai Hi", jathi="Tisra", difficulty="beginner"),

            # Kathak Adavus / Tukdas
            Adavu(name="Tatkar", dance_form=DanceForm.KATHAK,
                  description="Basic footwork pattern - foundation of Kathak",
                  steps=["Stand straight", "Stamp right heel", "Stamp left heel", "Increase speed gradually"],
                  count_pattern="Ta Thei Thei Tat", jathi="Teental (16 beats)", difficulty="beginner"),
            Adavu(name="Chakkar", dance_form=DanceForm.KATHAK,
                  description="Spinning technique - signature of Kathak",
                  steps=["Fix gaze on one point", "Push off with right foot", "Spot the point", "Complete rotation"],
                  count_pattern="Continuous", jathi="Variable", difficulty="advanced"),
            Adavu(name="Tora", dance_form=DanceForm.KATHAK,
                  description="Short rhythmic composition of footwork",
                  steps=["Begin with tabla bol", "Execute footwork pattern", "End on sam (first beat)"],
                  count_pattern="Dha Dhin Dhin Dha", jathi="Teental", difficulty="intermediate"),
            Adavu(name="Paran", dance_form=DanceForm.KATHAK,
                  description="Rhythmic composition using pakhawaj bols",
                  steps=["Start on sam", "Follow pakhawaj pattern", "Mix footwork with hand gestures", "End on sam"],
                  count_pattern="Dha Ge Ti Na", jathi="Teental", difficulty="advanced"),

            # Odissi Adavus
            Adavu(name="Chauka", dance_form=DanceForm.ODISSI,
                  description="Square stance - masculine posture of Odissi",
                  steps=["Feet apart, toes pointing out", "Bend knees outward", "Spine straight", "Arms in Alapadma at sides"],
                  count_pattern="Dhei Ta Dhei Ta", jathi="Ektali", difficulty="beginner"),
            Adavu(name="Tribhangi", dance_form=DanceForm.ODISSI,
                  description="Three-bend pose - signature of Odissi",
                  steps=["Shift hip to one side", "Bend torso opposite", "Head tilts to hip side", "Create S-curve"],
                  count_pattern="Ta Ka Dhimi", jathi="Variable", difficulty="intermediate"),
            Adavu(name="Bhumi Pranam", dance_form=DanceForm.ODISSI,
                  description="Earth salutation - opening of Odissi dance",
                  steps=["Stand in Samabhanga", "Bend forward touching floor", "Rise gracefully", "End in Tribhangi"],
                  count_pattern="Slow", jathi="Ektali", difficulty="beginner"),

            # Kuchipudi Adavus
            Adavu(name="Jati", dance_form=DanceForm.KUCHIPUDI,
                  description="Rhythmic syllable pattern danced with footwork",
                  steps=["Aramandi position", "Follow jati syllables with stamps", "Coordinate hand gestures", "End with flourish"],
                  count_pattern="Taka Dhimi", jathi="Adi tala", difficulty="intermediate"),
            Adavu(name="Tarangam", dance_form=DanceForm.KUCHIPUDI,
                  description="Dancing on the rim of a brass plate",
                  steps=["Stand on brass plate edges", "Balance in Aramandi", "Stamp on plate rim", "Maintain balance while moving"],
                  count_pattern="Taka Jham", jathi="Adi tala", difficulty="advanced"),

            # Mohiniyattam Adavus
            Adavu(name="Taganam", dance_form=DanceForm.MOHINIYATTAM,
                  description="Basic stepping pattern of Mohiniyattam",
                  steps=["Gentle Aramandi", "Step right with swaying motion", "Arms flow like waves", "Step left matching rhythm"],
                  count_pattern="Tai Ya Tai Hi", jathi="Chempata", difficulty="beginner"),
            Adavu(name="Jaganam", dance_form=DanceForm.MOHINIYATTAM,
                  description="Gliding steps with body sway",
                  steps=["Begin in slight Aramandi", "Glide sideways", "Body sways like coconut palm", "Arms follow body naturally"],
                  count_pattern="Tai Tai Ta", jathi="Chempata", difficulty="intermediate"),
        ]

    def _load_expressions(self) -> list[Expression]:
        """Navarasas - Nine primary emotions in classical dance."""
        return [
            Expression(name="Shringara", sanskrit_name="Shringara", description="Love/Beauty - the king of rasas, depicting romantic love",
                       facial_elements="Soft eyes, gentle smile, raised eyebrows, glowing face"),
            Expression(name="Hasya", sanskrit_name="Hasya", description="Laughter/Comedy - depicting humor and joy",
                       facial_elements="Wide smile, eyes crinkled, slight head tilt, relaxed face"),
            Expression(name="Karuna", sanskrit_name="Karuna", description="Compassion/Sorrow - depicting sadness and pathos",
                       facial_elements="Drooping eyes, downturned mouth, furrowed brow, tears"),
            Expression(name="Raudra", sanskrit_name="Raudra", description="Fury/Anger - depicting rage and indignation",
                       facial_elements="Wide fierce eyes, flared nostrils, clenched jaw, red face"),
            Expression(name="Veera", sanskrit_name="Veera", description="Heroism/Courage - depicting bravery and determination",
                       facial_elements="Broad chest, firm gaze, confident expression, raised chin"),
            Expression(name="Bhayanaka", sanskrit_name="Bhayanaka", description="Fear/Terror - depicting fright",
                       facial_elements="Wide eyes, trembling lips, contracted body, looking around"),
            Expression(name="Bibhatsa", sanskrit_name="Bibhatsa", description="Disgust/Aversion - depicting revulsion",
                       facial_elements="Wrinkled nose, squinted eyes, turned face, contracted lips"),
            Expression(name="Adbhuta", sanskrit_name="Adbhuta", description="Wonder/Amazement - depicting astonishment",
                       facial_elements="Wide open eyes, raised eyebrows, open mouth, expanded face"),
            Expression(name="Shanta", sanskrit_name="Shanta", description="Peace/Tranquility - depicting serenity and calm",
                       facial_elements="Half-closed eyes, serene smile, relaxed face, gentle demeanor"),
        ]

    def get_form_details(self, form: DanceForm) -> dict:
        return self._form_details.get(form, {})

    def get_adavus(self, form: DanceForm | None = None) -> list[Adavu]:
        if form is None:
            return self._adavus
        return [a for a in self._adavus if a.dance_form == form]

    def get_expressions(self) -> list[Expression]:
        return self._expressions

    def get_adavu(self, name: str) -> Adavu | None:
        for a in self._adavus:
            if a.name.lower() == name.lower():
                return a
        return None
