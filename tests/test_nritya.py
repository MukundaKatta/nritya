"""Tests for Nritya."""
import pytest
from nritya.dance.forms import DanceFormDatabase
from nritya.dance.poses import DancePoseLibrary
from nritya.dance.mudras import MudraDatabase
from nritya.analyzer.pose import PoseAnalyzer
from nritya.analyzer.corrector import DanceCorrector
from nritya.models import DanceForm, MudraType


class TestMudraDatabase:
    def test_28_asamyuta(self):
        db = MudraDatabase()
        assert len(db.get_asamyuta()) == 28

    def test_24_samyuta(self):
        db = MudraDatabase()
        assert len(db.get_samyuta()) == 24

    def test_get_mudra(self):
        db = MudraDatabase()
        m = db.get_mudra("Anjali")
        assert m is not None
        assert m.mudra_type == MudraType.SAMYUTA

    def test_search_by_usage(self):
        db = MudraDatabase()
        results = db.search_by_usage("prayer")
        assert len(results) >= 1


class TestDanceFormDatabase:
    def test_all_five_forms(self):
        db = DanceFormDatabase()
        for form in DanceForm:
            details = db.get_form_details(form)
            assert "origin" in details

    def test_adavus_per_form(self):
        db = DanceFormDatabase()
        bh_adavus = db.get_adavus(DanceForm.BHARATANATYAM)
        assert len(bh_adavus) >= 5

    def test_navarasas(self):
        db = DanceFormDatabase()
        assert len(db.get_expressions()) == 9


class TestDancePoseLibrary:
    def test_30_plus_poses(self):
        lib = DancePoseLibrary()
        assert len(lib.get_all_poses()) >= 30

    def test_get_pose(self):
        lib = DancePoseLibrary()
        p = lib.get_pose("Aramandi")
        assert p is not None
        assert p.dance_form == DanceForm.BHARATANATYAM

    def test_poses_by_form(self):
        lib = DancePoseLibrary()
        for form in DanceForm:
            poses = lib.get_poses_by_form(form)
            assert len(poses) >= 2, f"{form.value} has too few poses"


class TestPoseAnalyzer:
    def test_perfect_pose(self):
        lib = DancePoseLibrary()
        ref = lib.get_pose("Aramandi")
        observed = {a.joint_name: a.angle_degrees for a in ref.joint_angles}
        analyzer = PoseAnalyzer()
        result = analyzer.analyze(ref, observed)
        assert result.overall_score >= 95
        assert len(result.corrections) == 0

    def test_imperfect_pose(self):
        lib = DancePoseLibrary()
        ref = lib.get_pose("Aramandi")
        observed = {a.joint_name: a.angle_degrees + 30 for a in ref.joint_angles}
        analyzer = PoseAnalyzer()
        result = analyzer.analyze(ref, observed)
        assert result.overall_score < 95
        assert len(result.corrections) > 0


class TestDanceCorrector:
    def test_correct_pose(self):
        corrector = DanceCorrector()
        observed = {"left_knee": 130, "right_knee": 130, "spine": 180}
        result = corrector.correct_pose("Aramandi", observed)
        assert result is not None

    def test_find_closest_pose(self):
        corrector = DanceCorrector()
        observed = {"left_knee": 110, "right_knee": 110, "spine": 180}
        pose, score = corrector.find_closest_pose(observed, DanceForm.BHARATANATYAM)
        assert pose is not None
        assert score > 0

    def test_practice_sequence(self):
        corrector = DanceCorrector()
        seq = corrector.get_practice_sequence(DanceForm.BHARATANATYAM, "beginner")
        assert len(seq) >= 1
